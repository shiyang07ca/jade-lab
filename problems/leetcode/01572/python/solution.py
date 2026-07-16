# Created by shiyang07ca at 2023/08/11 00:22
# leetgo: dev
# https://leetcode.cn/problems/matrix-diagonal-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
        for j in range(n - 1, -1, -1):
            ans += mat[j][n - j - 1]
        if n % 2:
            ans -= mat[n // 2][n // 2]
        return ans


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().diagonalSum(mat)

    print("\noutput:", serialize(ans))
