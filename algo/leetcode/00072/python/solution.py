# Created by shiyang07ca at 2026/10/01 01:19
# leetgo: 1.4.17
# https://leetcode.cn/problems/edit-distance/

from functools import cache
from typing import *

from leetgo_py import *

# @lc code=begin

# TODO


# 链接：https://leetcode.cn/problems/edit-distance/solutions/2133222/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-uo5q/
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            # 把 s[:i] 转换成 t[:j]
            if i == 0:
                return j
            if j == 0:
                return i

            if s[i - 1] == t[j - 1]:
                return dfs(i - 1, j - 1)

            delete = dfs(i - 1, j) + 1
            insert = dfs(i, j - 1) + 1
            replace = dfs(i - 1, j - 1) + 1
            return min(delete, insert, replace)

        return dfs(len(s), len(t))

    # 递推
    def minDistance1(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        # dp[i][j] 表示把 s[:i] 转换成 t[:j] 的最少操作数
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # s[:i] 转换成空字符串：删除 i 次
        for i in range(n + 1):
            dp[i][0] = i

        # 空字符串转换成 t[:j]：插入 j 次
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete = dp[i - 1][j] + 1
                    insert = dp[i][j - 1] + 1
                    replace = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(delete, insert, replace)

        return dp[n][m]

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().minDistance(word1, word2)
    print("\noutput:", serialize(ans, "integer"))
