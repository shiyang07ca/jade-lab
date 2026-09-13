"""早期并查集实现，保留用于与 ``algorithms.DisjointSet`` 比较。

原实现会在 import 时分配一千万个整数。本实验把存储改为显式初始化，避免仅导入文件就占用大量内存；接口和
全局数组写法仍保留，以便分析它与封装后的稳定实现之间的差异。
"""

import unittest


parent: list[int] = []
component_sizes: list[int] = []


def initialize(size: int) -> None:
    global parent, component_sizes
    parent = list(range(size))
    component_sizes = [1] * size


def find(element: int) -> int:
    if parent[element] != element:
        parent[element] = find(parent[element])
    return parent[element]


def union(left: int, right: int) -> None:
    left_root, right_root = find(left), find(right)
    if left_root == right_root:
        return
    parent[left_root] = right_root
    component_sizes[right_root] += component_sizes[left_root]


class TestGlobalUnionFind(unittest.TestCase):
    def setUp(self) -> None:
        initialize(6)

    def test_components(self) -> None:
        union(0, 1)
        union(1, 2)
        union(3, 4)
        union(3, 5)

        self.assertEqual(find(0), find(2))
        self.assertEqual(find(3), find(5))
        self.assertNotEqual(find(0), find(3))


if __name__ == "__main__":
    unittest.main()
