# Created by shiyang07ca at 2024/10/20 12:45
# leetgo: dev
# https://leetcode.cn/problems/smallest-range-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = nums[-1] - nums[0] - 2 * k
        return x if x > 0 else 0


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRangeI(nums, k)
    print("\noutput:", serialize(ans, "integer"))
