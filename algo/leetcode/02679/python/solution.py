from __future__ import annotations

# Created by shiyang07ca at 2023/07/04 13:00
# leetgo: dev
# https://leetcode.cn/problems/sum-in-a-matrix/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:

    def matrixSum(self, nums: list[list[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        ans = 0
        for col in zip(*nums):
            print(col)
            ans += max(col)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixSum(nums)

    print("\noutput:", serialize(ans))
