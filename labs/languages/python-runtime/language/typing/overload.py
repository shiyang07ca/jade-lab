"""Connect literal arguments to precise return types with ``typing.overload``."""

from typing import Any, Literal, TypeVar, overload


T = TypeVar("T")


@overload
def foo(value: Any, flag: Literal[1]) -> int:
    ...


@overload
def foo(value: Any, flag: Literal[2]) -> str:
    ...


@overload
def foo(value: Any, flag: Literal[3]) -> list[Any]:
    ...


@overload
def foo(value: T, flag: object) -> T:
    ...


def foo(value: Any, flag: object) -> Any:
    """Apply the operation described by ``flag``; overloads serve type checkers."""
    if flag == 1:
        return int(value)
    if flag == 2:
        return str(value)
    if flag == 3:
        return [value]
    return value
