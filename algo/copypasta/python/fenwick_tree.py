"""Fenwick tree for point additions and range sums."""

from collections.abc import Sequence


class FenwickTree:
    """Use 0-based point indexes and half-open sum ranges."""

    def __init__(self, values: int | Sequence[int]) -> None:
        if isinstance(values, int):
            if values < 0:
                raise ValueError("size must be non-negative")
            items = [0] * values
        else:
            items = list(values)
        self._tree = [0] * (len(items) + 1)
        for index, value in enumerate(items):
            self.add(index, value)

    def __len__(self) -> int:
        return len(self._tree) - 1

    def add(self, index: int, delta: int) -> None:
        if not 0 <= index < len(self):
            raise IndexError("index is outside the tree")
        index += 1
        while index < len(self._tree):
            self._tree[index] += delta
            index += index & -index

    def prefix_sum(self, end: int) -> int:
        """Return the sum of ``[0:end]``."""
        if not 0 <= end <= len(self):
            raise IndexError("end is outside the tree")
        total = 0
        while end:
            total += self._tree[end]
            end -= end & -end
        return total

    def range_sum(self, start: int, end: int) -> int:
        if not 0 <= start <= end <= len(self):
            raise IndexError("range is outside the tree")
        return self.prefix_sum(end) - self.prefix_sum(start)
