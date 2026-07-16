# Created by shiyang07ca at 2023/07/26 13:37
# leetgo: dev
# https://leetcode.cn/problems/handling-sum-queries-after-update/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: Segment Tree
# template

"""
通过线段树维护数组 nums1 的区间和

定义线段树每个节点为 Node，每个节点包含如下属性：

* l: 节点的左端点，下标从 1 开始

* r: 节点的右端点，下标从 1 开始

* s: 节点的区间和

* lazy：节点的懒标记


线段树主要有以下几个操作：
 * build(u, l, r)：建立线段树

 * pushdown(u): 下传懒标记

 * pushup(u): 用子节点的信息更新父节点的信息

 * modify(u, l, r)：修改区间和，本题中是反转区间中的每个数，
   那么区间和 s = r - l + 1 - s

 * query(u, l, r): 查询区间和

我们先算出数组 nums2 的所有数之和，记为 s。

执行操作 1：调用 modify(1, l+1, r+1)
执行操作 2：更新 s = s + p*query(1, l, n)
执行操作 3：将 s 加入答案数据即可



https://leetcode.cn/problems/handling-sum-queries-after-update/solutions/2359125/python3javacgo-yi-ti-yi-jie-xian-duan-sh-maq2/
"""


class Node:
    def __init__(self):
        self.l = self.r = 0
        self.s = self.lazy = 0


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l == r:
            self.tr[u].s = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def modify(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            self.tr[u].lazy ^= 1
            self.tr[u].s = self.tr[u].r - self.tr[u].l + 1 - self.tr[u].s
            return
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if l <= mid:
            self.modify(u << 1, l, r)
        if r > mid:
            self.modify(u << 1 | 1, l, r)
        self.pushup(u)

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].s
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        res = 0
        if l <= mid:
            res += self.query(u << 1, l, r)
        if r > mid:
            res += self.query(u << 1 | 1, l, r)
        return res

    def pushup(self, u):
        self.tr[u].s = self.tr[u << 1].s + self.tr[u << 1 | 1].s

    def pushdown(self, u):
        if self.tr[u].lazy:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            self.tr[u << 1].s = mid - self.tr[u].l + 1 - self.tr[u << 1].s
            self.tr[u << 1].lazy ^= 1
            self.tr[u << 1 | 1].s = self.tr[u].r - mid - self.tr[u << 1 | 1].s
            self.tr[u << 1 | 1].lazy ^= 1
            self.tr[u].lazy ^= 1


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().handleQuery(nums1, nums2, queries)

    print("\noutput:", serialize(ans))
