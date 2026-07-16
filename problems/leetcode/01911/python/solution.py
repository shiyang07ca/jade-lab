# Created by shiyang07ca at 2023/07/11 13:04
# leetgo: dev
# https://leetcode.cn/problems/maximum-alternating-subsequence-sum/

from functools import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


class Solution:
    def maxAlternatingSum1(self, nums: List[int]) -> int:
        n = len(nums)
        op = [1, -1]

        @cache
        def dfs(i, j):
            if i == n:
                return 0
            return max(dfs(i + 1, j), op[j] * nums[i] + dfs(i + 1, j ^ 1))

        return dfs(0, 0)

    # 链接：https://leetcode.cn/problems/maximum-alternating-subsequence-sum/solutions/2339030/python3javacgotypescript-yi-ti-yi-jie-do-22yp/
    # 定义 f[i] 表示从前 i 个元素选出子序列，且最后一个元素为奇数下表的最大交替和
    # 定义 g[i] 表示从前 i 个元素选出子序列，且最后一个元素为偶数下表的最大交替和
    #             f[i] = max(g[i - 1] - x, f[i - 1])
    #             g[i] = max(f[i - 1] + x, g[i - 1])
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            f[i] = max(g[i - 1] - x, f[i - 1])
            g[i] = max(f[i - 1] + x, g[i - 1])
        return g[n]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxAlternatingSum(nums)

    print("\noutput:", serialize(ans))
