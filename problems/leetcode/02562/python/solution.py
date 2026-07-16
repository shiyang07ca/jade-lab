# Created by shiyang07ca at 2023/10/12 13:07
# leetgo: dev
# https://leetcode.cn/problems/find-the-array-concatenation-value/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        i, j = 0, len(nums) - 1
        while i < j:
            ans += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            ans += nums[i]
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findTheArrayConcVal(nums)

    print("\noutput:", serialize(ans))
