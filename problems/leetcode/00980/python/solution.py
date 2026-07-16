# Created by shiyang07ca at 2023/08/04 12:59
# leetgo: dev
# https://leetcode.cn/problems/unique-paths-iii/

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: Backtracking


class Solution:
    # 链接：https://leetcode.cn/problems/unique-paths-iii/solutions/2372252/liang-chong-fang-fa-hui-su-zhuang-tai-ya-26py/
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int, left: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0:
                return 0  # 不合法
            if grid[x][y] == 2:  # 到达终点
                return left == 0  # 必须访问所有的无障碍方格
            grid[x][y] = -1  # 标记成访问过，因为题目要求「不能重复通过同一个方格」
            ans = (
                dfs(x - 1, y, left - 1)
                + dfs(x, y - 1, left - 1)
                + dfs(x + 1, y, left - 1)
                + dfs(x, y + 1, left - 1)
            )
            grid[x][y] = 0  # 恢复现场
            return ans

        cnt0 = sum(row.count(0) for row in grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:  # 起点
                    return dfs(i, j, cnt0 + 1)  # +1 把起点也算上


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().uniquePathsIII(grid)

    print("\noutput:", serialize(ans))
