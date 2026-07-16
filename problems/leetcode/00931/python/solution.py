# Created by shiyang07ca at 2023/07/13 10:02
# leetgo: dev
# https://leetcode.cn/problems/minimum-falling-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: dp


class Solution:
    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return min(matrix[0])
        pre = matrix[0]
        for row in matrix[1:]:
            new = [0] * n
            for j, x in enumerate(row):
                if j == 0:
                    new[j] = x + min(pre[j], pre[j + 1])
                elif j == n - 1:
                    new[j] = x + min(pre[j], pre[j - 1])
                else:
                    new[j] = x + min(pre[j - 1], pre[j], pre[j + 1])
            pre = new
        return min(pre)

    # 链接：https://leetcode.cn/problems/minimum-falling-path-sum/solutions/2341851/cong-di-gui-dao-di-tui-jiao-ni-yi-bu-bu-2cwkb/
    # 记忆化搜索
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # dfs(r, c) 表示从 matrix[r][c] 出发，向上走到第一行的最小路径和
        @cache  # 记忆化搜索
        def dfs(r: int, c: int) -> int:
            if c < 0 or c >= n:  # 出界
                return inf
            if r == 0:  # 到达第一行
                return matrix[0][c]
            return (
                min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]
            )

        return min(dfs(n - 1, i) for i in range(n))  # 枚举起点，取最小值

    # 递推
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [[inf] * (n + 2) for _ in range(n)]
        f[0][1 : n + 1] = matrix[0]
        for r in range(1, n):
            for c in range(n):
                f[r][c + 1] = (
                    min(f[r - 1][c], f[r - 1][c + 1], f[r - 1][c + 2]) + matrix[r][c]
                )
        return min(f[-1])


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(matrix)

    print("\noutput:", serialize(ans))
