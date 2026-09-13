"""Sliding-window maximum backed by a monotone deque."""

from collections import deque
from collections.abc import Sequence


def sliding_window_max[T](values: Sequence[T], window: int) -> list[T]:
    """Return each fixed window's maximum in O(n) time and O(window) space."""
    if not isinstance(window, int) or isinstance(window, bool):
        raise TypeError("window must be an integer")
    if window < 1 or window > len(values):
        raise ValueError("window must be between 1 and len(values)")

    candidates: deque[int] = deque()
    result: list[T] = []
    for index, value in enumerate(values):
        while candidates and candidates[0] <= index - window:
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index >= window - 1:
            result.append(values[candidates[0]])
    return result
