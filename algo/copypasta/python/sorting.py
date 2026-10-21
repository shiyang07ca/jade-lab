"""Comparison sorting algorithms."""

from collections.abc import Sequence
from random import randrange


def quickselect[T](values: list[T], k: int) -> T:
    """原地选择升序下标 k 的元素；期望 O(n)，最坏 O(n²)，额外空间 O(1)。"""
    if not 0 <= k < len(values):
        raise IndexError("k out of range")

    left, right = 0, len(values)
    while True:
        pivot = values[randrange(left, right)]
        lower, current, upper = left, left, right
        # [left, lower) < pivot，[lower, current) == pivot，[upper, right) > pivot。
        while current < upper:
            if values[current] < pivot:
                values[lower], values[current] = values[current], values[lower]
                lower += 1
                current += 1
            elif values[current] > pivot:
                upper -= 1
                values[current], values[upper] = values[upper], values[current]
                # 换入的元素尚未检查，current 不动。
            else:
                current += 1

        # k 始终是原数组下标，只缩小搜索区间。
        if k < lower:
            right = lower
        elif k >= upper:
            left = upper
        else:
            return values[k]


def merge_sort[T](values: Sequence[T]) -> list[T]:
    """Return a stable sorted copy in O(n log n) time."""
    result = list(values)
    buffer = result.copy()

    def sort(left: int, right: int) -> None:
        if right - left <= 1:
            return
        middle = (left + right) // 2
        sort(left, middle)
        sort(middle, right)
        first, second = left, middle
        for output in range(left, right):
            if second >= right or (first < middle and result[first] <= result[second]):
                buffer[output] = result[first]
                first += 1
            else:
                buffer[output] = result[second]
                second += 1
        result[left:right] = buffer[left:right]

    sort(0, len(result))
    return result


def quick_sort[T](values: Sequence[T]) -> list[T]:
    """Return a sorted copy using in-place three-way partitioning."""
    result = list(values)

    def sort(left: int, right: int) -> None:
        if left >= right:
            return
        pivot = result[(left + right) // 2]
        lower, current, upper = left, left, right
        while current <= upper:
            if result[current] < pivot:
                result[lower], result[current] = result[current], result[lower]
                lower += 1
                current += 1
            elif result[current] > pivot:
                result[current], result[upper] = result[upper], result[current]
                upper -= 1
            else:
                current += 1
        sort(left, lower - 1)
        sort(upper + 1, right)

    sort(0, len(result) - 1)
    return result
