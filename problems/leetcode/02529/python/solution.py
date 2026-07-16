# Created by shiyang07ca at 2024/04/09 13:02
# leetgo: dev
# https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/

from bisect import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumCount(nums)

    print("\noutput:", serialize(ans))
