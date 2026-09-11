#!/usr/bin/env python3
"""Jade Lab 的模块发现、环境诊断和检查入口。"""

from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import tomllib
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Sequence
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "modules.toml"
SCRATCH = ROOT / ".scratch"

KINDS = {"learning", "package", "problems", "lab", "tool", "reference"}
KIND_ROOTS = {
    "learning": "learning",
    "package": "packages",
    "problems": "problems",
    "lab": "labs",
    "tool": "tools",
    "reference": "references",
}
STATUSES = {"active", "external", "incomplete", "legacy", "pinned", "stable"}
DEFAULT_VISIBLE_STATUSES = {"active", "stable"}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER_PATTERN = re.compile(r"\{([a-z_]+)\}")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
UNFINISHED_PATTERN = re.compile(r"\b(?:TODO|FIXME|NotImplementedError)\b")


class CatalogError(ValueError):
    """模块目录不符合仓库规则。"""


@dataclass(frozen=True)
class Module:
    id: str
    path: PurePosixPath
    kind: str
    status: str
    summary: str
    default_check: bool
    checks: tuple[tuple[str, ...], ...]

    @property
    def directory(self) -> Path:
        return ROOT.joinpath(*self.path.parts)


@dataclass(frozen=True)
class Catalog:
    modules: tuple[Module, ...]
    runtimes: dict[str, str]


class LocalLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "link", "script"}:
            return
        attribute = "href" if tag in {"a", "link"} else "src"
        for name, value in attrs:
            if name == attribute and value:
                self.links.append(value)


def _relative_path(value: Any, *, field: str) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise CatalogError(f"{field} must be a non-empty string")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or str(path) != value:
        raise CatalogError(f"{field} must be a normalized repository-relative path: {value!r}")
    return path


def load_catalog(path: Path = CATALOG_PATH) -> Catalog:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise CatalogError(f"cannot read {path}: {exc}") from exc

    if data.get("schema") != 1:
        raise CatalogError("modules.toml must declare schema = 1")
    raw_modules = data.get("modules")
    if not isinstance(raw_modules, list) or not raw_modules:
        raise CatalogError("modules.toml must contain at least one [[modules]] entry")

    seen_ids: set[str] = set()
    seen_paths: set[PurePosixPath] = set()
    modules: list[Module] = []
    for index, raw in enumerate(raw_modules, start=1):
        if not isinstance(raw, dict):
            raise CatalogError(f"modules entry {index} must be a table")
        module_id = raw.get("id")
        if not isinstance(module_id, str) or not ID_PATTERN.fullmatch(module_id):
            raise CatalogError(f"modules entry {index} has invalid id: {module_id!r}")
        module_path = _relative_path(raw.get("path"), field=f"{module_id}.path")
        kind = raw.get("kind")
        status = raw.get("status")
        summary = raw.get("summary")
        default_check = raw.get("default_check", False)
        raw_checks = raw.get("checks", [])

        if module_id in seen_ids:
            raise CatalogError(f"duplicate module id: {module_id}")
        if module_path in seen_paths:
            raise CatalogError(f"duplicate module path: {module_path}")
        if kind not in KINDS:
            raise CatalogError(f"{module_id}.kind must be one of {sorted(KINDS)}")
        expected_root = KIND_ROOTS[kind]
        if not module_path.parts or module_path.parts[0] != expected_root:
            raise CatalogError(
                f"{module_id}.path must be under {expected_root}/ for kind {kind}"
            )
        if kind in {"learning", "package", "problems", "tool", "reference"} and len(
            module_path.parts
        ) != 2:
            raise CatalogError(f"{module_id}.path must identify one module under {expected_root}/")
        if kind == "lab" and len(module_path.parts) < 3:
            raise CatalogError(f"{module_id}.path must identify a lab under labs/<area>/")
        if status not in STATUSES:
            raise CatalogError(f"{module_id}.status must be one of {sorted(STATUSES)}")
        if not isinstance(summary, str) or not summary.strip():
            raise CatalogError(f"{module_id}.summary must be a non-empty string")
        if not isinstance(default_check, bool):
            raise CatalogError(f"{module_id}.default_check must be a boolean")
        if not isinstance(raw_checks, list):
            raise CatalogError(f"{module_id}.checks must be an array")

        checks: list[tuple[str, ...]] = []
        for check_index, raw_check in enumerate(raw_checks, start=1):
            if not isinstance(raw_check, list) or not raw_check:
                raise CatalogError(f"{module_id}.checks[{check_index}] must be a non-empty argv array")
            if not all(isinstance(arg, str) and arg for arg in raw_check):
                raise CatalogError(f"{module_id}.checks[{check_index}] contains an invalid argument")
            unknown = {
                placeholder
                for arg in raw_check
                for placeholder in PLACEHOLDER_PATTERN.findall(arg)
                if placeholder not in {"module", "root", "scratch"}
            }
            if unknown:
                raise CatalogError(
                    f"{module_id}.checks[{check_index}] has unknown placeholders: {sorted(unknown)}"
                )
            checks.append(tuple(raw_check))

        if default_check and not checks:
            raise CatalogError(f"{module_id} is a default check but has no checks")
        if status == "stable" and not checks:
            raise CatalogError(f"stable module {module_id} must define checks")
        if kind == "package" and status != "stable":
            raise CatalogError(f"package module {module_id} must be stable")
        if kind == "package" and not default_check:
            raise CatalogError(f"package module {module_id} must be part of the default check")

        seen_ids.add(module_id)
        seen_paths.add(module_path)
        modules.append(
            Module(
                id=module_id,
                path=module_path,
                kind=kind,
                status=status,
                summary=summary.strip(),
                default_check=default_check,
                checks=tuple(checks),
            )
        )

    raw_runtimes = data.get("runtimes", {})
    if not isinstance(raw_runtimes, dict) or not all(
        isinstance(key, str) and isinstance(value, str) and value
        for key, value in raw_runtimes.items()
    ):
        raise CatalogError("[runtimes] must contain non-empty string values")
    return Catalog(modules=tuple(modules), runtimes=dict(raw_runtimes))


def _print_table(rows: Sequence[Sequence[str]], headers: Sequence[str]) -> None:
    widths = [len(header) for header in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))
    template = "  ".join(f"{{:<{width}}}" for width in widths)
    print(template.format(*headers))
    print(template.format(*("─" * width for width in widths)))
    for row in rows:
        print(template.format(*row))


def command_list(args: argparse.Namespace, catalog: Catalog) -> int:
    use_default_visibility = not args.all and args.kind is None and args.status is None
    modules = [
        module
        for module in catalog.modules
        if (not use_default_visibility or module.status in DEFAULT_VISIBLE_STATUSES)
        and (args.kind is None or module.kind == args.kind)
        and (args.status is None or module.status == args.status)
    ]
    rows = [
        (
            module.id,
            module.kind,
            module.status,
            "yes" if module.default_check else "",
            str(module.path),
            module.summary,
        )
        for module in modules
    ]
    _print_table(rows, ("ID", "KIND", "STATUS", "DEFAULT", "PATH", "SUMMARY"))
    print(f"\n{len(modules)} modules")
    return 0


def _run_capture(argv: Sequence[str], *, cwd: Path = ROOT) -> tuple[int, str]:
    try:
        completed = subprocess.run(
            argv,
            cwd=cwd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    except OSError as exc:
        return 127, str(exc)
    return completed.returncode, completed.stdout.strip()


def _mise_tools() -> tuple[dict[str, str], list[str]]:
    config = tomllib.loads((ROOT / "mise.toml").read_text(encoding="utf-8"))
    expected = config.get("tools", {})
    if not isinstance(expected, dict):
        return {}, ["mise.toml [tools] is invalid"]
    code, output = _run_capture(("mise", "current"))
    if code != 0:
        return {}, [f"mise current failed: {output}"]
    current: dict[str, str] = {}
    for line in output.splitlines():
        key, separator, version = line.partition(" ")
        if separator:
            current[key] = version.strip()

    errors: list[str] = []
    for tool, wanted in expected.items():
        if not isinstance(wanted, str):
            errors.append(f"unsupported mise version declaration for {tool}")
            continue
        actual = current.get(tool)
        if actual is None:
            errors.append(f"mise tool is not installed: {tool} {wanted}")
            continue
        if not actual.startswith(wanted):
            errors.append(f"mise tool version mismatch: {tool} wants {wanted}, current is {actual}")
    return current, errors


def _submodule_errors() -> tuple[list[str], str]:
    code, output = _run_capture(("git", "submodule", "status", "--recursive"))
    if code != 0:
        return [f"git submodule status failed: {output}"], output
    errors: list[str] = []
    for line in output.splitlines():
        marker = line[:1]
        path = line[42:].split(" ", 1)[0] if len(line) > 42 else line
        if marker == "-":
            errors.append(f"submodule is not initialized: {path}")
        elif marker == "+":
            errors.append(f"submodule is not at the recorded commit: {path}")
        elif marker == "U":
            errors.append(f"submodule has a merge conflict: {path}")
    return errors, output


def _repository_shape_errors(catalog: Catalog) -> list[str]:
    errors: list[str] = []
    for name in ("README.md", "CONTEXT.md", "mise.toml", "modules.toml"):
        if not (ROOT / name).is_file():
            errors.append(f"missing repository entry file: {name}")
    for module in catalog.modules:
        if module.kind == "reference":
            # 外部源码是否初始化是本机状态，不是仓库结构要求。gitlink 本身由
            # modules.toml、.gitmodules 和 Git index 共同记录，doctor 再检查工作树。
            continue
        if not module.directory.is_dir():
            errors.append(f"module path does not exist: {module.id} -> {module.path}")
        elif not (module.directory / "README.md").is_file():
            errors.append(f"module has no README.md: {module.id} -> {module.path}")

    indexed_paths = {module.path for module in catalog.modules}
    for root_name in ("learning", "packages", "problems", "tools"):
        root = ROOT / root_name
        if not root.is_dir():
            continue
        for child in sorted(path for path in root.iterdir() if path.is_dir()):
            relative = PurePosixPath(root_name, child.name)
            if relative not in indexed_paths:
                errors.append(f"unindexed module directory: {relative}")
    return errors


def _reference_config_errors(catalog: Catalog) -> list[str]:
    """Validate recorded reference metadata without initializing submodules."""
    errors: list[str] = []
    reference_paths = {
        str(module.path) for module in catalog.modules if module.kind == "reference"
    }

    code, output = _run_capture(("git", "ls-files", "--stage", "--", "references"))
    if code != 0:
        return [f"cannot inspect reference gitlinks: {output}"]
    gitlink_paths = {
        line.split("\t", 1)[1]
        for line in output.splitlines()
        if line.startswith("160000 ") and "\t" in line
    }

    code, output = _run_capture(
        ("git", "config", "-f", ".gitmodules", "--get-regexp", r"^submodule\..*\.path$")
    )
    if code not in {0, 1}:
        return [f"cannot inspect .gitmodules: {output}"]
    configured_paths = {
        line.split(maxsplit=1)[1]
        for line in output.splitlines()
        if len(line.split(maxsplit=1)) == 2
    }

    for path in sorted(reference_paths - gitlink_paths):
        errors.append(f"reference is not recorded as a Git submodule: {path}")
    for path in sorted(reference_paths - configured_paths):
        errors.append(f"reference is missing from .gitmodules: {path}")
    for path in sorted(gitlink_paths - reference_paths):
        errors.append(f"Git submodule is missing from modules.toml: {path}")
    return errors


def command_doctor(_args: argparse.Namespace, catalog: Catalog) -> int:
    failures: list[str] = []
    shape_errors = _repository_shape_errors(catalog)
    config_errors = _runtime_config_errors(catalog)
    catalog_errors = [*shape_errors, *config_errors]
    failures.extend(catalog_errors)
    if catalog_errors:
        print(f"[fail] catalog: {len(catalog_errors)} repository configuration errors")
        for error in catalog_errors:
            print(f"       {error}")
    else:
        print(f"[ok] catalog: {len(catalog.modules)} modules")

    if shutil.which("mise") is None:
        failures.append("mise is not available on PATH")
        print("[fail] mise: command not found")
    else:
        current, tool_errors = _mise_tools()
        failures.extend(tool_errors)
        if tool_errors:
            print(f"[fail] mise: {len(tool_errors)} tool errors")
        else:
            print(f"[ok] mise: {len(current)} configured tools installed")
        for error in tool_errors:
            print(f"       {error}")

    submodule_errors, submodule_output = _submodule_errors()
    failures.extend(submodule_errors)
    if submodule_errors:
        print(f"[fail] submodules: {len(submodule_errors)} errors")
        for error in submodule_errors:
            print(f"       {error}")
    else:
        count = len([line for line in submodule_output.splitlines() if line.strip()])
        print(f"[ok] submodules: {count} at recorded commits")

    bash_image = catalog.runtimes.get("bash_image")
    if bash_image:
        if shutil.which("docker") is None:
            print(f"[warn] Bash course: Docker is unavailable; target runtime is {bash_image}")
        else:
            code, _ = _run_capture(("docker", "image", "inspect", bash_image))
            if code == 0:
                print(f"[ok] Bash course image: {bash_image}")
            else:
                print(f"[warn] Bash course image is not cached; run `mise run bash --version`: {bash_image}")

    native_bash = os.environ.get("BASH_VERSION")
    if not native_bash and shutil.which("bash"):
        code, output = _run_capture(("bash", "--version"))
        if code == 0:
            native_bash = output.splitlines()[0]
    if native_bash:
        print(f"[info] host Bash: {native_bash}")

    free_bytes = shutil.disk_usage(ROOT).free
    print(f"[info] free disk: {free_bytes / (1024**3):.1f} GiB")
    if failures:
        print(f"\ndoctor found {len(failures)} blocking errors", file=sys.stderr)
        return 1
    print("\ndoctor passed")
    return 0


def _git_owned_files(prefixes: Sequence[str]) -> list[Path]:
    argv = ["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", *prefixes]
    code, output = _run_capture(argv)
    if code != 0:
        raise RuntimeError(output)
    return [ROOT / line for line in output.splitlines() if line]


def _link_target(link: str, source: Path) -> Path | None:
    link = link.strip()
    if link.startswith("<") and link.endswith(">"):
        link = link[1:-1]
    # Markdown 允许 `(path "title")`；本仓库路径不含空格。
    link = link.split(maxsplit=1)[0]
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path)
    if path.startswith("/"):
        return None
    return (source.parent / path).resolve()


def _documentation_errors() -> list[str]:
    errors: list[str] = []
    prefixes = [
        "README.md",
        "CONTRIBUTING.md",
        "CONTEXT.md",
        "docs",
        "learning",
        "packages",
        "labs",
        "problems",
        "tools",
    ]
    for path in _git_owned_files(prefixes):
        if not path.is_file() or "references" in path.parts:
            continue
        suffix = path.suffix.lower()
        if suffix == ".md":
            text = path.read_text(encoding="utf-8")
            links = MARKDOWN_LINK_PATTERN.findall(text)
        elif suffix == ".html":
            parser = LocalLinkParser()
            parser.feed(path.read_text(encoding="utf-8"))
            links = parser.links
        else:
            continue
        for link in links:
            target = _link_target(link, path)
            if target is not None and not target.exists():
                errors.append(f"broken local link: {path.relative_to(ROOT)} -> {link}")
    return errors


def _package_errors() -> list[str]:
    errors: list[str] = []
    text_suffixes = {
        ".c",
        ".cc",
        ".cpp",
        ".go",
        ".h",
        ".hpp",
        ".java",
        ".js",
        ".py",
        ".rs",
        ".sh",
    }
    for path in _git_owned_files(("packages",)):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        errors.extend(_package_source_errors(path.relative_to(ROOT), text))
    return errors


def _package_source_errors(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    if not text.strip() and path.name != "__init__.py":
        errors.append(f"empty source file in package: {path}")
    for line_number, line in enumerate(text.splitlines(), start=1):
        if UNFINISHED_PATTERN.search(line):
            errors.append(f"unfinished marker in package: {path}:{line_number}")
    return errors


def _bash_course_errors(catalog: Catalog) -> list[str]:
    lesson_dir = ROOT / "learning/bash/lessons"
    lessons = sorted(lesson_dir.glob("*.html"))
    errors: list[str] = []
    if len(lessons) != 15:
        errors.append(f"Bash course expects 15 lessons, found {len(lessons)}")
    expected_runtime = catalog.runtimes.get("bash_image", "")
    expected_version = catalog.runtimes.get("bash_version", "")
    audit_pattern = re.compile(
        r'<meta\s+name="course-audit"\s+content="\d{4}-\d{2}-\d{2};\s*([^\"]+)">'
    )
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        audit_match = audit_pattern.search(text)
        if audit_match is None:
            errors.append(f"Bash lesson has no audit marker: {lesson.relative_to(ROOT)}")
        elif expected_version and expected_version not in audit_match.group(1):
            errors.append(f"Bash lesson does not declare {expected_version}: {lesson.relative_to(ROOT)}")
        if "TODO" in text or "FIXME" in text:
            errors.append(f"Bash lesson contains unfinished marker: {lesson.relative_to(ROOT)}")
    if not expected_runtime:
        errors.append("modules.toml does not pin the Bash course image")
    return errors


def _runtime_config_errors(catalog: Catalog) -> list[str]:
    errors: list[str] = []
    try:
        config = tomllib.loads((ROOT / "mise.toml").read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return [f"cannot read mise.toml for runtime comparison: {exc}"]

    tools = config.get("tools", {})
    environment = config.get("env", {})
    expected_go = catalog.runtimes.get("go_version")
    if expected_go and tools.get("go") != expected_go:
        errors.append(
            f"Go runtime differs between modules.toml ({expected_go}) and mise.toml "
            f"({tools.get('go')})"
        )
    expected_bash_image = catalog.runtimes.get("bash_image")
    if expected_bash_image and environment.get("JADE_BASH_IMAGE") != expected_bash_image:
        errors.append("Bash image differs between modules.toml and mise.toml")
    return errors


def repository_errors(catalog: Catalog) -> list[str]:
    errors = _repository_shape_errors(catalog)
    errors.extend(_reference_config_errors(catalog))
    errors.extend(_runtime_config_errors(catalog))
    errors.extend(_documentation_errors())
    errors.extend(_package_errors())
    errors.extend(_bash_course_errors(catalog))
    return errors


def command_policy(_args: argparse.Namespace, catalog: Catalog) -> int:
    errors = repository_errors(catalog)
    if errors:
        print(f"[fail] repository policy: {len(errors)} errors", file=sys.stderr)
        for error in errors:
            print(f"       {error}", file=sys.stderr)
        return 1
    print("[ok] repository policy")
    return 0


def _expand_check(argv: Sequence[str], module: Module) -> tuple[str, ...]:
    values = {
        "module": str(module.directory),
        "root": str(ROOT),
        "scratch": str(SCRATCH),
    }
    return tuple(arg.format_map(values) for arg in argv)


def _select_modules(args: argparse.Namespace, catalog: Catalog) -> list[Module]:
    by_id = {module.id: module for module in catalog.modules}
    if args.modules:
        missing = [module_id for module_id in args.modules if module_id not in by_id]
        if missing:
            raise CatalogError(f"unknown module ids: {', '.join(missing)}")
        selected = [by_id[module_id] for module_id in args.modules]
    elif args.all:
        selected = [module for module in catalog.modules if module.checks]
    else:
        selected = [module for module in catalog.modules if module.default_check]
    without_checks = [module.id for module in selected if not module.checks]
    if without_checks:
        raise CatalogError(f"modules have no automated checks: {', '.join(without_checks)}")
    return selected


def command_check(args: argparse.Namespace, catalog: Catalog) -> int:
    modules = _select_modules(args, catalog)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    for module in modules:
        print(f"\n==> {module.id} ({module.path})", flush=True)
        if not module.directory.is_dir():
            failure = f"{module.id}: module directory does not exist: {module.path}"
            failures.append(failure)
            print(f"[fail] {failure}", file=sys.stderr)
            if not args.keep_going:
                return 1
            continue
        for raw_check in module.checks:
            check = _expand_check(raw_check, module)
            print(f"$ {shlex.join(check)}", flush=True)
            try:
                completed = subprocess.run(check, cwd=module.directory, check=False)
            except OSError as exc:
                failure = f"{module.id}: cannot run {check[0]}: {exc}"
                failures.append(failure)
                print(f"[fail] {failure}", file=sys.stderr)
                if not args.keep_going:
                    return 1
                break
            if completed.returncode != 0:
                failure = f"{module.id}: {shlex.join(check)} exited {completed.returncode}"
                failures.append(failure)
                print(f"[fail] {failure}", file=sys.stderr)
                if not args.keep_going:
                    return completed.returncode or 1
                break
        else:
            print(f"[ok] {module.id}")

    if failures:
        print(f"\n{len(failures)} module checks failed", file=sys.stderr)
        return 1
    print(f"\nall {len(modules)} module checks passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List Jade Lab modules, diagnose the environment, and run real module checks."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="list repository modules")
    list_parser.add_argument("--kind", choices=sorted(KINDS))
    list_parser.add_argument("--status", choices=sorted(STATUSES))
    list_parser.add_argument(
        "--all",
        action="store_true",
        help="include non-active modules when no explicit filter is given",
    )
    list_parser.set_defaults(handler=command_list)

    doctor_parser = subparsers.add_parser("doctor", help="diagnose tools and pinned references")
    doctor_parser.set_defaults(handler=command_doctor)

    policy_parser = subparsers.add_parser("policy", help="validate repository-wide policy")
    policy_parser.set_defaults(handler=command_policy)

    check_parser = subparsers.add_parser("check", help="run repository policy and module checks")
    check_parser.add_argument("modules", nargs="*", metavar="MODULE")
    check_parser.add_argument("--all", action="store_true", help="check every module with commands")
    check_parser.add_argument(
        "--keep-going", action="store_true", help="continue with other modules after a failure"
    )
    check_parser.set_defaults(handler=command_check)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "all", False) and getattr(args, "modules", []):
        parser.error("--all cannot be combined with module ids")
    try:
        catalog = load_catalog()
        return args.handler(args, catalog)
    except (CatalogError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
