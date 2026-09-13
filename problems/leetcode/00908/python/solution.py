from __future__ import annotations

# Created by shiyang07ca at 2024/10/20 12:45
# leetgo: dev
# https://leetcode.cn/problems/smallest-range-i/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        nums.sort()
        x = nums[-1] - nums[0] - 2 * k
        return x if x > 0 else 0


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRangeI(nums, k)
    print("\noutput:", serialize(ans, "integer"))
