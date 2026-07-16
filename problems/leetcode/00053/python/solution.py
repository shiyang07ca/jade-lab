# Created by shiyang07ca at 2023/11/20 21:38
# leetgo: dev
# https://leetcode.cn/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i < 0:
                return -inf

            return max(nums[i], dfs(i - 1) + nums[i])

        return max(dfs(i) for i in range(n))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)

    print("\noutput:", serialize(ans))
