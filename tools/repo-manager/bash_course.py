#!/usr/bin/env python3
"""Validate the Bash course against its pinned runtime."""

from __future__ import annotations

import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).resolve().parent / "fixtures/bash-course-smoke.sh"
EXERCISE_SCRIPTS = sorted((ROOT / "learning/bash/exercises").glob("**/*.sh"))


def run(command: list[str]) -> int:
    print(f"$ {' '.join(command)}", flush=True)
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    catalog = tomllib.loads((ROOT / "modules.toml").read_text(encoding="utf-8"))
    image = catalog["runtimes"]["bash_image"]
    expected_version = catalog["runtimes"]["bash_version"]

    scripts = [FIXTURE, *EXERCISE_SCRIPTS]
    commands = [
        ["shellcheck", "--shell=bash", *(str(script) for script in scripts)],
        ["shfmt", "-d", *(str(script) for script in scripts)],
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{ROOT}:/workspace:ro",
            "-w",
            "/workspace",
            image,
            "bash",
            "-n",
            "/workspace/tools/repo-manager/fixtures/bash-course-smoke.sh",
        ],
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{ROOT}:/workspace:ro",
            "-w",
            "/workspace",
            image,
            "bash",
            "/workspace/learning/bash/exercises/log-analyzer/test.sh",
        ],
        [
            "docker",
            "run",
            "--rm",
            "-e",
            f"EXPECTED_BASH_VERSION={expected_version}",
            "-v",
            f"{ROOT}:/workspace:ro",
            "-w",
            "/workspace",
            image,
            "bash",
            "/workspace/tools/repo-manager/fixtures/bash-course-smoke.sh",
        ],
    ]
    for command in commands:
        code = run(command)
        if code != 0:
            return code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
