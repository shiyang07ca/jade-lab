"""Binary search on sorted sequences."""

from collections.abc import Sequence


def lower_bound[T](values: Sequence[T], target: T) -> int:
    """Return the first index whose value is at least ``target``."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


def upper_bound[T](values: Sequence[T], target: T) -> int:
    """Return the first index whose value is greater than ``target``."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle
    return left


def binary_search[T](values: Sequence[T], target: T) -> int | None:
    """Return the first matching index, or ``None`` when absent."""
    index = lower_bound(values, target)
    return index if index < len(values) and values[index] == target else None
