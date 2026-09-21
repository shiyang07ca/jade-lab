#!/usr/bin/env python3
"""检查指定 LeetCode 题目的静态质量和本地测试。"""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path
from typing import cast

MODULE = Path(__file__).resolve().parent
ROOT = MODULE.parents[1]


def parse_args() -> str:
    parser = argparse.ArgumentParser(
        description="Check one LeetCode question without scanning the whole problem set."
    )
    _ = parser.add_argument("qid", help="question id, such as 88, 00088, or LCP-33")
    return cast(str, parser.parse_args().qid)


def normalize_qid(qid: str) -> tuple[str, str]:
    if not qid or Path(qid).name != qid or qid in {".", ".."}:
        raise ValueError("qid must be a single question identifier")
    if qid.isdecimal():
        numeric_qid = str(int(qid))
        return numeric_qid.zfill(5), numeric_qid
    return qid, qid


def run(command: list[str], *, cwd: Path) -> None:
    print(f"[leetcode-check] $ {shlex.join(command)}")
    result = subprocess.run(command, cwd=cwd, check=False)
    if result.returncode:
        raise SystemExit(result.returncode)


def check_python(qid: str, solution: Path) -> None:
    run(["uv", "run", "--frozen", "basedpyright", str(solution)], cwd=MODULE)
    run(["uv", "run", "--frozen", "ruff", "check", str(solution)], cwd=MODULE)
    committed_test = solution.with_name("test_solution.py")
    if committed_test.is_file():
        run(["uv", "run", "--frozen", "pytest", str(committed_test)], cwd=MODULE)
    else:
        run(["leetgo", "test", qid, "--lang", "python", "--local"], cwd=MODULE)


def check_go(qid: str, solution: Path) -> None:
    result = subprocess.run(
        ["gofmt", "-d", str(solution)],
        cwd=MODULE,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.returncode or result.stdout:
        raise SystemExit(result.returncode or 1)
    committed_test = solution.with_name("solution_test.go")
    if committed_test.is_file():
        relative_package = f"./{solution.parent.relative_to(MODULE)}"
        run(["go", "test", relative_package], cwd=MODULE)
    else:
        run(["leetgo", "test", qid, "--lang", "go", "--local"], cwd=MODULE)


def main() -> int:
    qid = parse_args()
    try:
        directory_name, runner_qid = normalize_qid(qid)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    directory = MODULE / directory_name

    if not directory.is_dir():
        print(f"error: question directory not found: {directory}", file=sys.stderr)
        return 2

    checks = 0
    python_solution = directory / "python" / "solution.py"
    if python_solution.is_file():
        check_python(runner_qid, python_solution)
        checks += 1

    go_solution = directory / "go" / "solution.go"
    if go_solution.is_file():
        check_go(runner_qid, go_solution)
        checks += 1

    if checks == 0:
        print(f"error: no supported solution found in {directory}", file=sys.stderr)
        return 2

    print(f"[leetcode-check] passed question={runner_qid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
