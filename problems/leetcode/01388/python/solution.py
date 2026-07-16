# Created by shiyang07ca at 2023/08/18 13:21
# leetgo: dev
# https://leetcode.cn/problems/pizza-with-3n-slices/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/pizza-with-3n-slices/solutions/2393650/python3javacgotypescript-yi-ti-yi-jie-do-mhhj/
    def maxSizeSlices(self, slices: List[int]) -> int:
        def g(nums: List[int]) -> int:
            m = len(nums)
            f = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, min(n + 1, i + 1)):
                    f[i][j] = max(
                        f[i - 1][j], (f[i - 2][j - 1] if i > 2 else 0) + nums[i - 1]
                    )
            return f[m][n]

        n = len(slices) // 3
        a, b = g(slices[:-1]), g(slices[1:])
        return max(a, b)

    # 链接：https://leetcode.cn/problems/pizza-with-3n-slices/solutions/2393770/ji-yi-hua-sou-suo-jie-jue-da-jia-jie-she-sora/
    def maxSizeSlices2(self, slices: List[int]) -> int:
        n = len(slices)
        m = n // 3

        # 环状序列相较于普通序列，相当于添加了一个限制：普通序列中的第一个和最后一个数不能同时选。
        # 第一个数不能选
        @cache
        def dfs1(i, c):
            if i >= n:
                return 0 if c == 0 else -inf
            res1 = dfs1(i + 1, c)
            res2 = dfs1(i + 2, c - 1) + slices[i]
            return max(res1, res2)

        # 最后一个数不能选
        @cache
        def dfs2(i, c):
            if i >= n - 1:
                return 0 if c == 0 else -inf
            res1 = dfs2(i + 1, c)
            res2 = dfs2(i + 2, c - 1) + slices[i]
            return max(res1, res2)

        return max(dfs1(1, m), dfs2(0, m))


# @lc code=end

if __name__ == "__main__":
    slices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSizeSlices(slices)

    print("\noutput:", serialize(ans))
