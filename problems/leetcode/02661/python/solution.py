# Created by shiyang07ca at 2023/12/01 12:50
# leetgo: dev
# https://leetcode.cn/problems/first-completely-painted-row-or-column/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        pos = {}
        for i, row in enumerate(mat):
            for j, n in enumerate(row):
                pos[n] = (i, j)

        row = [0 for _ in range(M)]
        col = [0 for _ in range(N)]
        for i, n in enumerate(arr):
            x, y = pos[n]
            row[x] += 1
            col[y] += 1
            if row[x] == N or col[y] == M:
                return i


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().firstCompleteIndex(arr, mat)

    print("\noutput:", serialize(ans))
