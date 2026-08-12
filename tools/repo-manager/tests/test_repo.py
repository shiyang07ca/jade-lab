from __future__ import annotations

import importlib.util
import io
import sys
import tempfile
import unittest
from argparse import Namespace
from contextlib import redirect_stdout
from pathlib import Path, PurePosixPath
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "repo.py"
SPEC = importlib.util.spec_from_file_location("jade_repo_manager", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
repo = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = repo
SPEC.loader.exec_module(repo)


VALID_CATALOG = """\
schema = 1

[runtimes]
bash_version = "5.3.15"

[[modules]]
id = "package-python-algorithms"
path = "packages/python-algorithms"
kind = "package"
status = "stable"
summary = "Python samples"
default_check = true
checks = [["python", "-m", "pytest", "{module}"]]
"""


class CatalogTests(unittest.TestCase):
    def load(self, text: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "modules.toml"
            path.write_text(text, encoding="utf-8")
            return repo.load_catalog(path)

    def test_loads_valid_catalog(self) -> None:
        catalog = self.load(VALID_CATALOG)

        self.assertEqual("5.3.15", catalog.runtimes["bash_version"])
        self.assertEqual("package-python-algorithms", catalog.modules[0].id)
        self.assertTrue(catalog.modules[0].default_check)

    def test_rejects_parent_path(self) -> None:
        invalid = VALID_CATALOG.replace(
            'path = "packages/python-algorithms"', 'path = "../python"'
        )

        with self.assertRaisesRegex(repo.CatalogError, "normalized repository-relative"):
            self.load(invalid)

    def test_rejects_unknown_placeholder(self) -> None:
        invalid = VALID_CATALOG.replace("{module}", "{workspace}")

        with self.assertRaisesRegex(repo.CatalogError, "unknown placeholders"):
            self.load(invalid)

    def test_rejects_path_outside_kind_root(self) -> None:
        invalid = VALID_CATALOG.replace(
            'path = "packages/python-algorithms"',
            'path = "labs/python-algorithms"',
        )

        with self.assertRaisesRegex(repo.CatalogError, "must be under packages/"):
            self.load(invalid)

    def test_rejects_duplicate_id(self) -> None:
        module_block = VALID_CATALOG.split("[[modules]]", 1)[1]
        duplicate = VALID_CATALOG + "\n[[modules]]" + module_block

        with self.assertRaisesRegex(repo.CatalogError, "duplicate module id"):
            self.load(duplicate)

    def test_package_module_must_be_stable_and_checked_by_default(self) -> None:
        not_stable = VALID_CATALOG.replace('status = "stable"', 'status = "active"')
        not_default = VALID_CATALOG.replace("default_check = true\n", "")

        with self.assertRaisesRegex(repo.CatalogError, "must be stable"):
            self.load(not_stable)
        with self.assertRaisesRegex(repo.CatalogError, "must be part of the default check"):
            self.load(not_default)


class ListTests(unittest.TestCase):
    def test_default_list_hides_non_active_statuses(self) -> None:
        stable = repo.Module(
            id="package-python-algorithms",
            path=PurePosixPath("packages/python-algorithms"),
            kind="package",
            status="stable",
            summary="Stable Python package",
            default_check=True,
            checks=(("true",),),
        )
        legacy = repo.Module(
            id="lab-legacy",
            path=PurePosixPath("labs/legacy"),
            kind="lab",
            status="legacy",
            summary="Legacy lab",
            default_check=False,
            checks=(),
        )
        catalog = repo.Catalog(modules=(stable, legacy), runtimes={})
        output = io.StringIO()

        with redirect_stdout(output):
            result = repo.command_list(
                Namespace(kind=None, status=None, all=False), catalog
            )

        self.assertEqual(0, result)
        self.assertIn("package-python-algorithms", output.getvalue())
        self.assertNotIn("lab-legacy", output.getvalue())

    def test_explicit_kind_shows_hidden_statuses(self) -> None:
        legacy = repo.Module(
            id="lab-legacy",
            path=PurePosixPath("labs/legacy"),
            kind="lab",
            status="legacy",
            summary="Legacy lab",
            default_check=False,
            checks=(),
        )
        output = io.StringIO()

        with redirect_stdout(output):
            result = repo.command_list(
                Namespace(kind="lab", status=None, all=False),
                repo.Catalog(modules=(legacy,), runtimes={}),
            )

        self.assertEqual(0, result)
        self.assertIn("lab-legacy", output.getvalue())


class LinkTests(unittest.TestCase):
    def test_resolves_relative_markdown_link_without_fragment(self) -> None:
        source = repo.ROOT / "docs/example.md"

        target = repo._link_target("../README.md#usage", source)

        self.assertEqual(repo.ROOT / "README.md", target)

    def test_ignores_remote_and_anchor_links(self) -> None:
        source = repo.ROOT / "README.md"

        self.assertIsNone(repo._link_target("https://go.dev/", source))
        self.assertIsNone(repo._link_target("#usage", source))

    def test_html_parser_collects_local_resources(self) -> None:
        parser = repo.LocalLinkParser()

        parser.feed('<a href="next.html">next</a><script src="../assets/quiz.js"></script>')

        self.assertEqual(["next.html", "../assets/quiz.js"], parser.links)


class CheckExpansionTests(unittest.TestCase):
    def test_expands_known_paths_without_shell(self) -> None:
        module = repo.Module(
            id="example",
            path=PurePosixPath("packages/python-algorithms"),
            kind="package",
            status="stable",
            summary="example",
            default_check=True,
            checks=(("tool", "{scratch}/out"),),
        )

        command = repo._expand_check(module.checks[0], module)

        self.assertEqual("tool", command[0])
        self.assertEqual(str(repo.ROOT / ".scratch/out"), command[1])


class PackagePolicyTests(unittest.TestCase):
    def test_rejects_empty_source_and_unfinished_marker(self) -> None:
        empty = repo._package_source_errors(Path("packages/python-algorithms/empty.py"), "")
        unfinished = repo._package_source_errors(
            Path("packages/python-algorithms/sample.py"), "value = 1  # TODO\n"
        )

        self.assertEqual(
            ["empty source file in package: packages/python-algorithms/empty.py"], empty
        )
        self.assertEqual(
            ["unfinished marker in package: packages/python-algorithms/sample.py:1"],
            unfinished,
        )

    def test_allows_empty_python_package_marker(self) -> None:
        errors = repo._package_source_errors(
            Path("packages/python-algorithms/topic/__init__.py"), ""
        )

        self.assertEqual([], errors)


class RepositoryConfigurationTests(unittest.TestCase):
    def test_runtime_versions_match_mise_configuration(self) -> None:
        catalog = repo.load_catalog()

        self.assertEqual([], repo._runtime_config_errors(catalog))

    def test_references_are_recorded_without_requiring_worktrees(self) -> None:
        catalog = repo.load_catalog()

        self.assertEqual([], repo._reference_config_errors(catalog))


class CommandSeparationTests(unittest.TestCase):
    def test_module_check_does_not_run_repository_policy(self) -> None:
        module = repo.Module(
            id="package-python-algorithms",
            path=PurePosixPath("packages/python-algorithms"),
            kind="package",
            status="stable",
            summary="Stable Python package",
            default_check=True,
            checks=(("true",),),
        )
        args = Namespace(modules=[module.id], all=False, keep_going=False)

        with mock.patch.object(
            repo, "repository_errors", side_effect=AssertionError("policy called")
        ):
            result = repo.command_check(
                args, repo.Catalog(modules=(module,), runtimes={})
            )

        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
