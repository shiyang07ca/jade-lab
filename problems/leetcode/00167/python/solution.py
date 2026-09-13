from __future__ import annotations

from bisect import bisect_left

# Created by shiyang07ca at 2023/07/08 21:49
# leetgo: dev
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def twoSum1(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i, x in enumerate(numbers):
            j = bisect_left(numbers, target - x, lo=i + 1)
            if j < n and numbers[j] == target - x:
                return [i + 1, j + 1]
        raise ValueError("no two-sum solution")

    # 链接：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/2335244/python3javacgotypescript-yi-ti-shuang-ji-a8kx/
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            x = numbers[i] + numbers[j]
            if x == target:
                return [i + 1, j + 1]
            if x < target:
                i += 1
            else:
                j -= 1
        raise ValueError("no two-sum solution")


# @lc code=end

if __name__ == "__main__":
    numbers: list[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(numbers, target)

    print("\noutput:", serialize(ans))
