import argparse
import shlex
import sys
from collections.abc import Callable, Sequence

from process_inspector.core import ProcessInfo, find_processes

Finder = Callable[[str], list[ProcessInfo]]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="查询匹配进程及其线程数")
    parser.add_argument("query", help="进程名称或命令行关键字")
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    finder: Finder = find_processes,
) -> int:
    args = build_parser().parse_args(argv)
    try:
        matches = finder(args.query)
    except ValueError as exc:
        print(f"参数错误: {exc}", file=sys.stderr)
        return 2
    if not matches:
        print(f"未找到进程: {args.query}", file=sys.stderr)
        return 1

    for process in matches:
        command = shlex.join(process.command)
        print(
            f"PID={process.pid} name={process.name} "
            f"threads={process.thread_count} command={command}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
