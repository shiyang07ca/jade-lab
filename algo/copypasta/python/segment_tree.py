"""Segment trees with explicit sum, minimum, and assignment operations."""

from collections.abc import Sequence
from math import inf


def _validate_range(size: int, left: int, right: int) -> None:
    if not 0 <= left < right <= size:
        raise IndexError("range must be non-empty and inside the tree")


class SumSegmentTree:
    """Point assignment and half-open range sums in O(log n)."""

    def __init__(self, values: Sequence[int]) -> None:
        if not values:
            raise ValueError("values must not be empty")
        self._size = len(values)
        leaf_count = 1
        while leaf_count < self._size:
            leaf_count *= 2
        self._leaf_count = leaf_count
        self._tree = [0] * (2 * leaf_count)
        self._tree[leaf_count : leaf_count + self._size] = values
        for node in range(leaf_count - 1, 0, -1):
            self._tree[node] = self._tree[node * 2] + self._tree[node * 2 + 1]

    def assign(self, index: int, value: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError("index is outside the tree")
        node = self._leaf_count + index
        self._tree[node] = value
        while node > 1:
            node //= 2
            self._tree[node] = self._tree[node * 2] + self._tree[node * 2 + 1]

    def range_sum(self, left: int, right: int) -> int:
        _validate_range(self._size, left, right)
        left += self._leaf_count
        right += self._leaf_count
        total = 0
        while left < right:
            if left & 1:
                total += self._tree[left]
                left += 1
            if right & 1:
                right -= 1
                total += self._tree[right]
            left //= 2
            right //= 2
        return total


class LazyMinSegmentTree:
    """Range addition and half-open range minimum queries in O(log n)."""

    def __init__(self, values: Sequence[int]) -> None:
        if not values:
            raise ValueError("values must not be empty")
        self._size = len(values)
        self._minimum = [0] * (4 * self._size)
        self._pending = [0] * (4 * self._size)
        self._build(1, 0, self._size, values)

    def _build(self, node: int, node_left: int, node_right: int, values: Sequence[int]) -> None:
        if node_right - node_left == 1:
            self._minimum[node] = values[node_left]
            return
        middle = (node_left + node_right) // 2
        self._build(node * 2, node_left, middle, values)
        self._build(node * 2 + 1, middle, node_right, values)
        self._minimum[node] = min(self._minimum[node * 2], self._minimum[node * 2 + 1])

    def _apply(self, node: int, delta: int) -> None:
        self._minimum[node] += delta
        self._pending[node] += delta

    def _push(self, node: int) -> None:
        if self._pending[node]:
            self._apply(node * 2, self._pending[node])
            self._apply(node * 2 + 1, self._pending[node])
            self._pending[node] = 0

    def add(self, left: int, right: int, delta: int) -> None:
        _validate_range(self._size, left, right)
        self._add(1, 0, self._size, left, right, delta)

    def _add(
        self,
        node: int,
        node_left: int,
        node_right: int,
        left: int,
        right: int,
        delta: int,
    ) -> None:
        if left <= node_left and node_right <= right:
            self._apply(node, delta)
            return
        self._push(node)
        middle = (node_left + node_right) // 2
        if left < middle:
            self._add(node * 2, node_left, middle, left, right, delta)
        if middle < right:
            self._add(node * 2 + 1, middle, node_right, left, right, delta)
        self._minimum[node] = min(self._minimum[node * 2], self._minimum[node * 2 + 1])

    def range_min(self, left: int, right: int) -> int:
        _validate_range(self._size, left, right)
        return self._range_min(1, 0, self._size, left, right)

    def _range_min(self, node: int, node_left: int, node_right: int, left: int, right: int) -> int:
        if left <= node_left and node_right <= right:
            return self._minimum[node]
        self._push(node)
        middle = (node_left + node_right) // 2
        result = inf
        if left < middle:
            result = min(result, self._range_min(node * 2, node_left, middle, left, right))
        if middle < right:
            result = min(
                result,
                self._range_min(node * 2 + 1, middle, node_right, left, right),
            )
        return int(result)


class RangeAssignSumTree:
    """Range assignment and half-open range sums in O(log n)."""

    def __init__(self, values: Sequence[int]) -> None:
        if not values:
            raise ValueError("values must not be empty")
        self._size = len(values)
        self._sum = [0] * (4 * self._size)
        self._pending: list[int | None] = [None] * (4 * self._size)
        self._build(1, 0, self._size, values)

    def _build(self, node: int, node_left: int, node_right: int, values: Sequence[int]) -> None:
        if node_right - node_left == 1:
            self._sum[node] = values[node_left]
            return
        middle = (node_left + node_right) // 2
        self._build(node * 2, node_left, middle, values)
        self._build(node * 2 + 1, middle, node_right, values)
        self._sum[node] = self._sum[node * 2] + self._sum[node * 2 + 1]

    def _apply(self, node: int, length: int, value: int) -> None:
        self._sum[node] = length * value
        self._pending[node] = value

    def _push(self, node: int, node_left: int, node_right: int) -> None:
        value = self._pending[node]
        if value is None or node_right - node_left == 1:
            return
        middle = (node_left + node_right) // 2
        self._apply(node * 2, middle - node_left, value)
        self._apply(node * 2 + 1, node_right - middle, value)
        self._pending[node] = None

    def assign(self, left: int, right: int, value: int) -> None:
        _validate_range(self._size, left, right)
        self._assign(1, 0, self._size, left, right, value)

    def _assign(
        self,
        node: int,
        node_left: int,
        node_right: int,
        left: int,
        right: int,
        value: int,
    ) -> None:
        if left <= node_left and node_right <= right:
            self._apply(node, node_right - node_left, value)
            return
        self._push(node, node_left, node_right)
        middle = (node_left + node_right) // 2
        if left < middle:
            self._assign(node * 2, node_left, middle, left, right, value)
        if middle < right:
            self._assign(node * 2 + 1, middle, node_right, left, right, value)
        self._sum[node] = self._sum[node * 2] + self._sum[node * 2 + 1]

    def range_sum(self, left: int, right: int) -> int:
        _validate_range(self._size, left, right)
        return self._range_sum(1, 0, self._size, left, right)

    def _range_sum(self, node: int, node_left: int, node_right: int, left: int, right: int) -> int:
        if left <= node_left and node_right <= right:
            return self._sum[node]
        self._push(node, node_left, node_right)
        middle = (node_left + node_right) // 2
        total = 0
        if left < middle:
            total += self._range_sum(node * 2, node_left, middle, left, right)
        if middle < right:
            total += self._range_sum(node * 2 + 1, middle, node_right, left, right)
        return total
