"""A minimal binary min-heap implementation."""

from collections.abc import Iterable


class MinHeap[T]:
    """Store comparable values with logarithmic insertion and removal."""

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._items: list[T] = []
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        return len(self._items)

    def push(self, value: T) -> None:
        """Insert one value."""
        self._items.append(value)
        self._swim_up(len(self._items) - 1)

    def peek(self) -> T:
        """Return the minimum value without removing it."""
        if not self._items:
            raise IndexError("peek from an empty heap")
        return self._items[0]

    def pop(self) -> T:
        """Remove and return the minimum value."""
        if not self._items:
            raise IndexError("remove from an empty heap")
        minimum = self._items[0]
        last = self._items.pop()
        if self._items:
            self._items[0] = last
            self._swim_down(0)
        return minimum

    def _swim_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self._items[parent] <= self._items[index]:
                return
            self._items[parent], self._items[index] = self._items[index], self._items[parent]
            index = parent

    def _swim_down(self, index: int) -> None:
        while True:
            left = index * 2 + 1
            if left >= len(self._items):
                return
            right = left + 1
            child = (
                right
                if right < len(self._items) and self._items[right] < self._items[left]
                else left
            )
            if self._items[index] <= self._items[child]:
                return
            self._items[index], self._items[child] = self._items[child], self._items[index]
            index = child
