# Created by shiyang07ca at 2023/09/16 00:00
# leetgo: dev
# https://leetcode.cn/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rob1(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(len(nums) - 1)

    # 递推
    def rob2(self, nums: List[int]) -> int:
        f = [0] * (len(nums) + 2)
        for i, x in enumerate(nums):
            f[i + 2] = max(f[i + 1], f[i] + x)
        return f[-1]

    # 空间优化
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)

    print("\noutput:", serialize(ans))
