"""在已排序序列中执行二分查找。"""

from collections.abc import Sequence
from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...
    def __le__(self, other: object, /) -> bool: ...


def lower_bound[T: Comparable](values: Sequence[T], target: T) -> int:
    """返回第一个值大于或等于 ``target`` 的下标；若不存在则返回序列长度。"""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


def upper_bound[T: Comparable](values: Sequence[T], target: T) -> int:
    """返回第一个值大于 ``target`` 的下标；若不存在则返回序列长度。"""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle
    return left


def binary_search[T: Comparable](values: Sequence[T], target: T) -> int | None:
    """返回 ``target`` 首次出现的下标；若不存在则返回 ``None``。"""
    index = lower_bound(values, target)
    return index if index < len(values) and values[index] == target else None
