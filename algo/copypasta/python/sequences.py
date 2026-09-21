"""Sequence algorithms."""


def fibonacci_sequence(length: int) -> list[int]:
    """Return the first ``length`` Fibonacci numbers, starting with 1, 1."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")
    result: list[int] = []
    previous, current = 0, 1
    for _ in range(length):
        result.append(current)
        previous, current = current, previous + current
    return result
