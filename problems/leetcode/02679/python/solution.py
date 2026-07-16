# Created by shiyang07ca at 2023/07/04 13:00
# leetgo: dev
# https://leetcode.cn/problems/sum-in-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:

    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        ans = 0
        for col in zip(*nums):
            print(col)
            ans += max(col)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixSum(nums)

    print("\noutput:", serialize(ans))
