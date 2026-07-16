# Created by shiyang07ca at 2024/05/07 08:44
# leetgo: dev
# https://leetcode.cn/problems/cherry-pickup-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/cherry-pickup-ii/solutions/2768158/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-i70v/
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i == m or j < 0 or j >= n or k < 0 or k >= n:
                return 0
            return (
                max(
                    dfs(i + 1, j2, k2)
                    for j2 in (j - 1, j, j + 1)
                    for k2 in (k - 1, k, k + 1)
                )
                + grid[i][j]
                + (grid[i][k] if k != j else 0)
            )

        return dfs(0, 0, n - 1)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cherryPickup(grid)
    print("\noutput:", serialize(ans, "integer"))
