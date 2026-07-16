"""
"""
"""
"""


"""

线段树

线段树是一棵二叉树，线段树上每个结点对应的是序列的一段区间，每一个叶子结点对应的
是序列的一个元素。

树上的每个节点都维护一个区间，根维护的是整个区间，每个节点维护的是父亲的区间二等
分后的其中一个子区间。

当有 n 个元素时，对区间的操作可以在 O(logn) 复杂度时间内完成。

另外，从二叉树结构上，可以看出线段树是一棵完美二叉树（Perfect Binary Tree），即
所有叶子的深度都相同，

并且每个节点要么是叶子，要么有 2 个子树。


ref:
https://www.desgard.com/algo/docs/part3/ch02/1-segment-tree-rmq/




lazy 线段树

问题：一个数组，更新一个子数组的值（都加上一个数、把子数组内的元素取反，...）
                查询一个子数组的值（求和，求最大值, ...）


两大思想
1. 挑选 O(n) 个特殊区间，使得任意一个区间可以拆分为 O(log n) 个特殊区间


"""


def build(o: int, l: int, r: int) -> None:
    if l == r:
        return
    m = (l + r) // 2
    build(o * 2, l, m)
    build(o * 2 + 1, m + 1, r)
    # maintain


# 更新 [L, R]
def update(o: int, l: int, r: int, L: int, R: int) -> None:
    if L <= l and r <= R:
        return


################################################################


# 链接：https://leetcode.cn/problems/range-module/description/


class Node:
    __slots__ = ["left", "right", "add", "v"]

    def __init__(self):
        self.left = None
        self.right = None
        self.add = 0
        self.v = False


class SegmentTree:
    __slots__ = ["root"]

    def __init__(self):
        self.root = Node()

    def modify(self, left, right, v, l=1, r=int(1e9), node=None):
        if node is None:
            node = self.root
        if l >= left and r <= right:
            if v == 1:
                node.add = 1
                node.v = True
            else:
                node.add = -1
                node.v = False
            return
        self.pushdown(node)
        mid = (l + r) >> 1
        if left <= mid:
            self.modify(left, right, v, l, mid, node.left)
        if right > mid:
            self.modify(left, right, v, mid + 1, r, node.right)
        self.pushup(node)

    def query(self, left, right, l=1, r=int(1e9), node=None):
        if node is None:
            node = self.root
        if l >= left and r <= right:
            return node.v
        self.pushdown(node)
        mid = (l + r) >> 1
        v = True
        if left <= mid:
            v = v and self.query(left, right, l, mid, node.left)
        if right > mid:
            v = v and self.query(left, right, mid + 1, r, node.right)
        return v

    def pushup(self, node):
        node.v = bool(node.left and node.left.v and node.right and node.right.v)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.add:
            node.left.add = node.right.add = node.add
            node.left.v = node.add == 1
            node.right.v = node.add == 1
            node.add = 0
