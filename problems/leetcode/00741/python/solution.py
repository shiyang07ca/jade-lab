# Created by shiyang07ca at 2024/05/06 09:27
# leetgo: dev
# https://leetcode.cn/problems/cherry-pickup/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    # 链接：https://leetcode.cn/problems/cherry-pickup/solutions/2766975/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-ruue/
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(t: int, j: int, k: int) -> int:
            # 不能出界，不能访问 -1 格子
            if (
                j < 0
                or k < 0
                or t < j
                or t < k
                or grid[t - j][j] < 0
                or grid[t - k][k] < 0
            ):
                return -inf
            if t == 0:  # 此时 j = k = 0
                return grid[0][0]
            return (
                max(
                    dfs(t - 1, j, k),
                    dfs(t - 1, j, k - 1),
                    dfs(t - 1, j - 1, k),
                    dfs(t - 1, j - 1, k - 1),
                )
                + grid[t - j][j]
                + (grid[t - k][k] if k != j else 0)
            )

        n = len(grid)
        return max(dfs(n * 2 - 2, n - 1, n - 1), 0)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cherryPickup(grid)
    print("\noutput:", serialize(ans, "integer"))
