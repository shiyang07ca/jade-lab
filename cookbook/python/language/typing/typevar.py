from typing import TypeVar, assert_type


def test_pari():
    T = TypeVar("T")
    U = TypeVar("U")

    def pair(first: T, second: U) -> tuple[T, U]:
        return (first, second)

    # def pair[T, U](first: T, second: U) -> tuple[T, U]:
    #     return (first, second)

    assert_type(pair(1, "2"), tuple[int, str])
