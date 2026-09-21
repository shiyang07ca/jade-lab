"""A binary min-heap."""

from collections.abc import Iterable


class MinHeap[T]:
    def __init__(self, values: Iterable[T] = ()) -> None:
        self._items = list(values)
        for index in range(len(self._items) // 2 - 1, -1, -1):
            self._sift_down(index)

    def __len__(self) -> int:
        return len(self._items)

    def push(self, value: T) -> None:
        self._items.append(value)
        index = len(self._items) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self._items[parent] <= self._items[index]:
                break
            self._items[parent], self._items[index] = self._items[index], self._items[parent]
            index = parent

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from an empty heap")
        return self._items[0]

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from an empty heap")
        minimum = self._items[0]
        last = self._items.pop()
        if self._items:
            self._items[0] = last
            self._sift_down(0)
        return minimum

    def _sift_down(self, index: int) -> None:
        while (left := index * 2 + 1) < len(self._items):
            right = left + 1
            child = (
                right
                if right < len(self._items) and self._items[right] < self._items[left]
                else left
            )
            if self._items[index] <= self._items[child]:
                break
            self._items[index], self._items[child] = self._items[child], self._items[index]
            index = child
