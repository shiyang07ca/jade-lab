# Created by shiyang07ca at 2024/05/26 19:15
# leetgo: dev
# https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/solutions/2790359/liang-chong-fang-fa-er-wei-qian-zhui-yi-689bf/
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] ^ s[i][j + 1] ^ s[i][j] ^ x
        return sorted(x for row in s[1:] for x in row[1:])[-k]


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestValue(matrix, k)
    print("\noutput:", serialize(ans, "integer"))
