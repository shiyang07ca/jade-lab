# Created by shiyang07ca at 2026/09/25 10:54
# leetgo: 1.4.17
# https://leetcode.cn/problems/maximal-square/

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalSquare(matrix)
    print("\noutput:", serialize(ans, "integer"))
