# Created by shiyang07ca at 2023/07/20 12:55
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-circular-subarray/

from functools import lru_cache as cache

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        if n == 1:
            return nums[0]

        @cache
        def dfs(j):
            if j == 0:
                return nums[j]
            else:
                return min(nums[j], dfs(j - 1) + nums[j])

        @cache
        def dfs2(j):
            if j == 0:
                return nums[j]
            else:
                return max(nums[j], dfs2(j - 1) + nums[j])

        mi = min(dfs(i) for i in range(n))
        ma = max(dfs2(i) for i in range(n))
        if s - mi == 0:
            return ma
        else:
            return max(s - mi, ma, s)

        # 链接：https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/2351107/mei-you-si-lu-yi-zhang-tu-miao-dong-pyth-ilqh/

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s = -inf  # 最大子数组和，不能为空
        min_s = 0  # 最小子数组和，可以为空
        max_f = min_f = 0
        for x in nums:
            # 以 nums[i-1] 结尾的子数组选或不选（取 max）+ x = 以 x 结尾的最大子数组和
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            # 以 nums[i-1] 结尾的子数组选或不选（取 min）+ x = 以 x 结尾的最小子数组和
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)
        if sum(nums) == min_s:
            return max_s
        return max(max_s, sum(nums) - min_s)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubarraySumCircular(nums)

    print("\noutput:", serialize(ans))
