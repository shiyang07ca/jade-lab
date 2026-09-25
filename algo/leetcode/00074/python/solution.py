# Created by shiyang07ca at 2026/09/25 11:14
# leetgo: 1.4.17
# https://leetcode.cn/problems/search-a-2d-matrix/

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            if x < target:
                left = mid + 1
            else:
                right = mid
        return False


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
