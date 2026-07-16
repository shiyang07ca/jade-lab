# Created by shiyang07ca at 2023/11/17 13:04
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-queries/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# 链接：https://leetcode.cn/problems/maximum-sum-queries/
class BinaryIndexedTree:
    __slots__ = ["n", "c"]

    def __init__(self, n: int):
        self.n = n
        self.c = [-1] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        mx = -1
        while x:
            mx = max(mx, self.c[x])
            x -= x & -x
        return mx


class Solution:
    def maximumSumQueries(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        nums = sorted(zip(nums1, nums2), key=lambda x: -x[0])
        nums2.sort()
        n, m = len(nums1), len(queries)
        ans = [-1] * m
        j = 0
        tree = BinaryIndexedTree(n)
        for i in sorted(range(m), key=lambda i: -queries[i][0]):
            x, y = queries[i]
            while j < n and nums[j][0] >= x:
                k = n - bisect_left(nums2, nums[j][1])
                tree.update(k, nums[j][0] + nums[j][1])
                j += 1
            k = n - bisect_left(nums2, y)
            ans[i] = tree.query(k)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumSumQueries(nums1, nums2, queries)

    print("\noutput:", serialize(ans))
