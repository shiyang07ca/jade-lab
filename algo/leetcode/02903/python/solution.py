from __future__ import annotations

# Created by shiyang07ca at 2024/05/25 22:44
# leetgo: dev
# https://leetcode.cn/problems/find-indices-with-index-and-value-difference-i/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        for i, row in enumerate(nums):
            for j in range(i, len(nums)):
                if (
                    abs(i - j) >= indexDifference
                    and abs(nums[i] - nums[j]) >= valueDifference
                ):
                    return [i, j]
        return [-1, -1]


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    indexDifference: int = deserialize("int", read_line())
    valueDifference: int = deserialize("int", read_line())
    ans = Solution().findIndices(nums, indexDifference, valueDifference)
    print("\noutput:", serialize(ans, "integer[]"))
