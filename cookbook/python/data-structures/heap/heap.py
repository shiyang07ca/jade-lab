r"""
Binary Heap. A min heap is a complete binary tree where each node is smaller than
its children. The root, therefore, is the minimum element in the tree. The min
heap uses an array to represent the data and operation. For example a min heap:

     4
   /   \
  50    7
 / \   /
55 90 87

Heap [0, 4, 50, 7, 55, 90, 87]

Method in class: insert, remove_min
For example insert(2) in a min heap:

     4                     4                     2
   /   \                 /   \                 /   \
  50    7      -->     50     2       -->     50    4
 / \   /  \           /  \   / \             /  \  /  \
55 90 87   2         55  90 87  7           55  90 87  7

For example remove_min() in a min heap:

     4                     87                    7
   /   \                 /   \                 /   \
  50    7      -->     50     7       -->     50    87
 / \   /              /  \                   /  \
55 90 87             55  90                 55  90

"""
from abc import ABCMeta, abstractmethod


class AbstractHeap(metaclass=ABCMeta):
    """Abstract Class for Binary Heap."""

    def __init__(self):
        """Pass."""

    @abstractmethod
    def swim_up(self, i):
        """Pass."""

    @abstractmethod
    def insert(self, val):
        """Pass."""

    @abstractmethod
    def swim_down(self, i):
        """Pass."""

    @abstractmethod
    def min_child_index(self, i):
        """Pass."""

    @abstractmethod
    def remove_min(self):
        """Pass."""


class BinaryHeap(AbstractHeap):
    """Binary Heap Class"""

    def __init__(self):
        self.current_size = 0
        self.heap = [0]

    def swim_up(self, i):
        while i // 2 > 0:
            # 如果子节点比父节点小，则交换
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def swim_down(self, i):
        while 2 * i < self.current_size:
            min_index = self.min_child_index(i)
            if self.heap[min_index] < self.heap[i]:
                self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]

            i = min_index

    def insert(self, val):
        self.heap.append(val)
        self.current_size = self.current_size + 1
        self.swim_up(self.current_size)
        # print(self.heap)

    def remove_min(self):
        ret = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
        # TODO
        self.swim_down(1)
        return ret

    def min_child_index(self, i):
        # 边界条件，没有右孩子
        if 2 * i + 1 > self.current_size:
            return 2 * i
        elif self.heap[2 * i + 1] < self.heap[2 * i]:
            return 2 * i + 1
        else:
            return 2 * i


import unittest


class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = BinaryHeap()
        self.min_heap.insert(4)
        self.min_heap.insert(50)
        self.min_heap.insert(7)
        self.min_heap.insert(55)
        self.min_heap.insert(90)
        self.min_heap.insert(87)

    def test_insert(self):
        # Before insert 2: [0, 4, 50, 7, 55, 90, 87]
        # After insert:    [0, 2, 50, 4, 55, 90, 87, 7]
        self.assertEqual(6, self.min_heap.current_size)
        self.min_heap.insert(2)
        self.assertEqual([0, 2, 50, 4, 55, 90, 87, 7], self.min_heap.heap)
        self.assertEqual(7, self.min_heap.current_size)

    def test_remove_min(self):
        ret = self.min_heap.remove_min()
        # Before remove_min : [0, 4, 50, 7,  55, 90, 87]
        # After remove_min:   [0, 7, 50, 87, 55, 90]
        # Test return value
        self.assertEqual(4, ret)
        self.assertEqual([0, 7, 50, 87, 55, 90], self.min_heap.heap)
        self.assertEqual(5, self.min_heap.current_size)


if __name__ == "__main__":
    # unittest.main()
    pass
