# Created by shiyang07ca at 2023/08/26 21:38
# leetgo: dev
# https://leetcode.cn/problems/summary-ranges/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
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
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().summaryRanges(nums)

    print("\noutput:", serialize(ans))
