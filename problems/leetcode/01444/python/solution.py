# Created by shiyang07ca at 2023/08/17 21:50
# leetgo: dev
# https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: 二维前缀和


# 链接：https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/solutions/2392051/ji-bai-100cong-di-gui-dao-di-tui-dao-you-dxz5/
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        ms = MatrixSum(pizza)
        m, n = len(pizza), len(pizza[0])

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(c: int, i: int, j: int) -> int:
            if c == 0:
                return 1 if ms.query(i, j, m, n) else 0
            res = 0
            for j2 in range(j + 1, n):  # 垂直切
                if ms.query(i, j, m, j2):  # 有苹果
                    res += dfs(c - 1, i, j2)
            for i2 in range(i + 1, m):  # 水平切
                if ms.query(i, j, i2, n):  # 有苹果
                    res += dfs(c - 1, i2, j)
            return res % MOD

        return dfs(k - 1, 0, 0)


# 二维前缀和模板（'A' 视作 1，'.' 视作 0）
class MatrixSum:
    def __init__(self, matrix: List[str]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + (x == "A")
        self.s = s

    # 返回左上角在 (r1,c1) 右下角在 (r2-1,c2-1) 的子矩阵元素和（类似前缀和的左闭右开）
    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2][c2] - self.s[r2][c1] - self.s[r1][c2] + self.s[r1][c1]


# @lc code=end

if __name__ == "__main__":
    pizza: List[str] = deserialize("List[str]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().ways(pizza, k)

    print("\noutput:", serialize(ans))
