#!/usr/bin/env python3
"""Validate the Bash course against its pinned runtime."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).resolve().parent / "fixtures/runtime-smoke.sh"
# The unfinished cleanup exercise is linted here; acceptance needs a supplied implementation.
EXERCISE_SCRIPTS = sorted((ROOT / "learning/bash/exercises").glob("**/*.sh"))


def run(command: list[str]) -> int:
    print(f"$ {' '.join(command)}", flush=True)
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    image = os.environ.get("JADE_BASH_IMAGE")
    expected_version = os.environ.get("JADE_BASH_VERSION")
    if not image or not expected_version:
        if shutil.which("mise"):
            os.chdir(ROOT)
            os.execvp("mise", ["mise", "exec", "--", "python", str(Path(__file__))])
        print(
            "error: mise is required to provide JADE_BASH_IMAGE and JADE_BASH_VERSION",
            file=sys.stderr,
        )
        return 2

    if shutil.which("docker") is None:
        print("error: Docker is required for the pinned Bash course runtime", file=sys.stderr)
        return 2
    if run(["docker", "info", "--format", "{{.ServerVersion}}"]):
        print("error: Docker daemon is unavailable", file=sys.stderr)
        return 2

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
            "/workspace/learning/bash/fixtures/runtime-smoke.sh",
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
            "/workspace/learning/bash/fixtures/runtime-smoke.sh",
        ],
    ]
    for command in commands:
        code = run(command)
        if code != 0:
            return code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
