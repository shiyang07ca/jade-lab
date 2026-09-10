#!/usr/bin/env python3
"""检查指定 LeetCode 题目的静态质量和本地测试。"""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path
from typing import cast

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "problems" / "leetcode"


def parse_args() -> str:
    parser = argparse.ArgumentParser(
        description="Check one LeetCode question without scanning the whole problem set."
    )
    _ = parser.add_argument("qid", help="question id, such as 88, 00088, or LCP-33")
    return cast(str, parser.parse_args().qid)


def question_dir(qid: str) -> Path:
    if not qid or Path(qid).name != qid or qid in {".", ".."}:
        raise ValueError("qid must be a single question identifier")
    directory_name = qid.zfill(5) if qid.isdecimal() else qid
    return MODULE / directory_name


def run(command: list[str], *, cwd: Path) -> None:
    print(f"[leetcode-check] $ {shlex.join(command)}")
    result = subprocess.run(command, cwd=cwd, check=False)
    if result.returncode:
        raise SystemExit(result.returncode)


def check_python(qid: str, solution: Path) -> None:
    run(["uv", "run", "--frozen", "basedpyright", str(solution)], cwd=MODULE)
    run(["uv", "run", "--frozen", "ruff", "check", str(solution)], cwd=MODULE)
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
    run(["leetgo", "test", qid, "--lang", "go", "--local"], cwd=MODULE)


def main() -> int:
    qid = parse_args()
    try:
        directory = question_dir(qid)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not directory.is_dir():
        print(f"error: question directory not found: {directory}", file=sys.stderr)
        return 2

    checks = 0
    python_solution = directory / "python" / "solution.py"
    if python_solution.is_file():
        check_python(qid, python_solution)
        checks += 1

    go_solution = directory / "go" / "solution.go"
    if go_solution.is_file():
        check_go(qid, go_solution)
        checks += 1

    if checks == 0:
        print(f"error: no supported solution found in {directory}", file=sys.stderr)
        return 2

    print(f"[leetcode-check] passed question={qid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
