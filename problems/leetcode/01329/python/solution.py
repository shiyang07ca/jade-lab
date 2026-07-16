# Created by shiyang07ca at 2024/04/29 00:00
# leetgo: dev
# https://leetcode.cn/problems/sort-the-matrix-diagonally/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/sort-the-matrix-diagonally/solutions/2760094/dui-jiao-xian-pai-xu-fu-yuan-di-pai-xu-p-uts8/
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for k in range(1 - n, m):  # k = i - j
            left_i, right_i = max(k, 0), min(k + n, m)
            a = sorted(mat[i][i - k] for i in range(left_i, right_i))
            for i in range(left_i, right_i):
                mat[i][i - k] = a[i - left_i]
        return mat


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().diagonalSort(mat)
    print("\noutput:", serialize(ans, "integer[][]"))
