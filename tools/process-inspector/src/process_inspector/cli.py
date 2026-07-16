import argparse

from process_inspector.core import find_processes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="查询匹配进程及其线程数")
    parser.add_argument("query", help="进程名称或命令行关键字")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    matches = find_processes(args.query)
    if not matches:
        print(f"未找到进程: {args.query}")
        return 1

    for process in matches:
        command = " ".join(process.command)
        print(
            f"PID={process.pid} name={process.name} "
            f"threads={process.thread_count} command={command}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
