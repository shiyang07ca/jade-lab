# Created by shiyang07ca at 2023/09/17 00:00
# leetgo: dev
# https://leetcode.cn/problems/house-robber-ii/

from functools import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i < 0:
                return 0
            return max(dfs(i - 1, j), dfs(i - 2, j) + ns[j][i])

        if len(nums) == 1:
            return nums[0]

        n = len(nums) - 2
        ns = [nums[1:], nums[:-1]]
        return max(dfs(n, 0), dfs(n, 1))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)

    print("\noutput:", serialize(ans))
