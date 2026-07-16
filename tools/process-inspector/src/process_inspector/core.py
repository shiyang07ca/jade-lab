from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Protocol

import psutil


class ProcessLike(Protocol):
    info: dict[str, object]

    def num_threads(self) -> int: ...


ProcessIterator = Callable[[list[str]], Iterable[ProcessLike]]


@dataclass(frozen=True)
class ProcessInfo:
    pid: int
    name: str
    thread_count: int
    command: tuple[str, ...]


def find_processes(
    query: str,
    process_iterator: ProcessIterator = psutil.process_iter,
) -> list[ProcessInfo]:
    normalized_query = query.strip().casefold()
    if not normalized_query:
        raise ValueError("process query must not be empty")

    matches: list[ProcessInfo] = []
    for process in process_iterator(["pid", "name", "cmdline"]):
        try:
            command = tuple(str(part) for part in (process.info.get("cmdline") or ()))
            name = str(process.info.get("name") or "")
            searchable = " ".join((name, *command)).casefold()
            if normalized_query not in searchable:
                continue

            matches.append(
                ProcessInfo(
                    pid=int(process.info["pid"]),
                    name=name,
                    thread_count=process.num_threads(),
                    command=command,
                )
            )
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            continue

    return sorted(matches, key=lambda item: item.pid)
