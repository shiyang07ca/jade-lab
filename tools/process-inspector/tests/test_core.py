from dataclasses import dataclass

import pytest

from process_inspector.core import find_processes


@dataclass
class FakeProcess:
    info: dict[str, object]
    threads: int

    def num_threads(self) -> int:
        return self.threads


def fake_iterator(_fields: list[str]):
    return [
        FakeProcess({"pid": 42, "name": "python", "cmdline": ["python", "worker.py"]}, 7),
        FakeProcess({"pid": 7, "name": "redis-server", "cmdline": ["redis-server"]}, 4),
        FakeProcess({"pid": 18, "name": "Python", "cmdline": ["python", "api.py"]}, 3),
    ]


def test_find_processes_matches_name_and_command_case_insensitively() -> None:
    matches = find_processes("PYTHON", fake_iterator)

    assert [(match.pid, match.thread_count) for match in matches] == [(18, 3), (42, 7)]


def test_find_processes_rejects_empty_query() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        find_processes("   ", fake_iterator)
