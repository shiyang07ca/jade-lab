from __future__ import annotations

# Created by shiyang07ca at 2024/03/14 23:00
# leetgo: dev
# https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        ans = nums[-1]
        i = len(nums) - 1
        while i >= 0:
            t = nums[i]
            while i > 0 and nums[i - 1] <= t:
                t += nums[i - 1]
                i -= 1
            ans = max(ans, t)
            i -= 1

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArrayValue(nums)

    print("\noutput:", serialize(ans))
