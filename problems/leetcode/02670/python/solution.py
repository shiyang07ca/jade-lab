# Created by shiyang07ca at 2024/01/31 13:07
# leetgo: dev
# https://leetcode.cn/problems/find-the-distinct-difference-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(len(set(nums[: i + 1])) - len(set(nums[i + 1 :])))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distinctDifferenceArray(nums)

    print("\noutput:", serialize(ans))
