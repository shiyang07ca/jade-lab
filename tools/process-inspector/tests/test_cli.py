from process_inspector.cli import main
from process_inspector.core import ProcessInfo


def test_cli_prints_matches_and_returns_success(capsys) -> None:
    def find(_query: str) -> list[ProcessInfo]:
        return [ProcessInfo(42, "python", 7, ("python", "worker job.py"))]

    result = main(["python"], finder=find)

    captured = capsys.readouterr()
    assert result == 0
    assert captured.err == ""
    assert captured.out == (
        "PID=42 name=python threads=7 command=python 'worker job.py'\n"
    )


def test_cli_reports_no_match_on_stderr(capsys) -> None:
    result = main(["missing"], finder=lambda _query: [])

    captured = capsys.readouterr()
    assert result == 1
    assert captured.out == ""
    assert captured.err == "未找到进程: missing\n"


def test_cli_maps_invalid_query_to_usage_error(capsys) -> None:
    def reject(_query: str) -> list[ProcessInfo]:
        raise ValueError("process query must not be empty")

    result = main(["   "], finder=reject)

    captured = capsys.readouterr()
    assert result == 2
    assert captured.out == ""
    assert captured.err == "参数错误: process query must not be empty\n"
