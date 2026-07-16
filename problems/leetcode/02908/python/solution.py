# Created by shiyang07ca at 2024/03/29 22:05
# leetgo: dev
# https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        ans = min(ans, nums[i] + nums[j] + nums[k])
        return ans if ans != inf else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumSum(nums)

    print("\noutput:", serialize(ans))
