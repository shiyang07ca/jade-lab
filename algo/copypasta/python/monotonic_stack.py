"""Monotonic-stack algorithms."""

from collections.abc import Sequence


def nearest_less_indices[T](values: Sequence[T]) -> list[tuple[int | None, int | None]]:
    """Return nearest strictly smaller indexes on both sides, including duplicates."""
    result: list[tuple[int | None, int | None]] = [(None, None)] * len(values)
    stack: list[list[int]] = []
    for index, value in enumerate(values):
        while stack and values[stack[-1][0]] > value:
            group = stack.pop()
            left = stack[-1][-1] if stack else None
            for popped in group:
                result[popped] = (left, index)
        if stack and values[stack[-1][0]] == value:
            stack[-1].append(index)
        else:
            stack.append([index])
    while stack:
        group = stack.pop()
        left = stack[-1][-1] if stack else None
        for popped in group:
            result[popped] = (left, None)
    return result


def next_greater_indices[T](values: Sequence[T]) -> list[int | None]:
    """Return each element's nearest strictly greater index to the right."""
    result: list[int | None] = [None] * len(values)
    stack: list[int] = []
    for index, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            result[stack.pop()] = index
        stack.append(index)
    return result
