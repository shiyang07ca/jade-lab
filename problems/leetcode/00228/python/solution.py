from __future__ import annotations

from itertools import pairwise

# Created by shiyang07ca at 2023/08/26 21:38
# leetgo: dev
# https://leetcode.cn/problems/summary-ranges/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        ans = [str(nums[0])]
        pre = nums[0]
        for a, b in pairwise(nums):
            if b - a == 1:
                ans[-1] = f"{pre}->{b}"
            else:
                pre = b
                ans.append(str(b))

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().summaryRanges(nums)

    print("\noutput:", serialize(ans))
