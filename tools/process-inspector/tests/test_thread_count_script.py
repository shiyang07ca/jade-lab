import os
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "thread-count.sh"


def install_fake_command(directory: Path, name: str, source: str) -> None:
    command = directory / name
    command.write_text(source, encoding="utf-8")
    command.chmod(0o755)


def run_script(fake_commands: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ | {"PATH": f"{fake_commands}:{os.environ['PATH']}"}
    return subprocess.run(
        ["bash", str(SCRIPT), "worker"],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )


def test_thread_count_propagates_pgrep_dependency_failure(tmp_path: Path) -> None:
    install_fake_command(
        tmp_path,
        "pgrep",
        """#!/usr/bin/env bash
printf 'pgrep dependency failed\n' >&2
exit 2
""",
    )
    install_fake_command(tmp_path, "ps", "#!/usr/bin/env bash\nexit 99\n")

    result = run_script(tmp_path)

    assert result.returncode == 2
    assert result.stdout == ""
    assert "pgrep dependency failed" in result.stderr
    assert "No process matched" not in result.stderr


def test_thread_count_skips_pid_that_disappears(tmp_path: Path) -> None:
    install_fake_command(tmp_path, "pgrep", "#!/usr/bin/env bash\nprintf '42\\n43\\n'\n")
    install_fake_command(
        tmp_path,
        "ps",
        """#!/usr/bin/env bash
if [[ $1 == -p && $2 == 42 ]]; then
    exit 1
fi
if [[ $1 == -p && $2 == 43 ]]; then
    printf 'python worker.py\n'
    exit 0
fi
if [[ $1 == -M && $2 == 43 ]]; then
    printf 'USER PID THREAD\nuser 43 1\nuser 43 2\n'
    exit 0
fi
exit 64
""",
    )

    result = run_script(tmp_path)

    assert result.returncode == 0
    assert result.stdout == "PID=43 threads=2 command=python worker.py\n"
    assert "Skipping PID 42" in result.stderr
