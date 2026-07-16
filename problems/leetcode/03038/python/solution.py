# Created by shiyang07ca at 2024/06/07 01:37
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        t = nums[0] + nums[1]
        ans = 1
        n = len(nums)
        i = 2
        while i < n:
            if i + 1 < n and t == (nums[i] + nums[i + 1]):
                ans += 1
                i += 2
            else:
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
