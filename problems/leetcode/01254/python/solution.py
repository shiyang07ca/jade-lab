# Created by shiyang07ca at 2023/06/18 23:03
# https://leetcode.cn/problems/number-of-closed-islands/

"""
1254. 统计封闭岛屿的数目 (Medium)
二维矩阵 `grid` 由 `0` （土地）和 `1` （水）组成。岛是由最大的4个方向连通的 `0` 组成的群，封闭岛是一
个 `完全` 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png)

```
输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1
,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
```

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/07/sample_4_1610.png)

```
输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1

```

**示例 3：**

```
输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2

```

**提示：**

- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <=1`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


# 链接：https://leetcode.cn/problems/number-of-closed-islands/solutions/2312631/python3javacgotypescript-yi-ti-shuang-ji-ttoe/
class Solution:
    def closedIsland1(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            res = int(0 < i < m - 1 and 0 < j < n - 1)
            grid[i][j] = 1
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    res &= dfs(x, y)
            return res

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        return sum(grid[i][j] == 0 and dfs(i, j) for i in range(m) for j in range(n))

    # 链接：https://leetcode.cn/problems/number-of-closed-islands/solutions/2312616/liang-chong-si-lu-xian-wai-hou-nei-chu-j-b1e4/
    def closedIsland2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def dfs(x: int, y: int) -> None:
            grid[x][y] = 1  # 标记 (x,y) 被访问，避免重复访问
            # 访问四方向的 0
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    dfs(i, j)

        for i in range(m):
            # 如果是第一行和最后一行，访问所有格子
            # 如果不是，只访问第一列和最后一列的格子
            step = 1 if i == 0 or i == m - 1 else n - 1
            for j in range(0, n, step):
                if grid[i][j] == 0:  # 从没有访问过的 0 出发
                    dfs(i, j)

        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:  # 从没有访问过的 0 出发
                    ans += 1  # 一定是封闭岛屿
                    dfs(i, j)
        return ans

    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def dfs(x: int, y: int) -> None:
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:  # 边界
                nonlocal closed
                closed = False  # 不是封闭岛屿
            grid[x][y] = 1  # 标记 (x,y) 被访问，避免重复访问
            # 访问四方向的 0
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    dfs(i, j)

        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:  # 从没有访问过的 0 出发
                    closed = True
                    dfs(i, j)
                    ans += closed
        return ans


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().closedIsland(grid)

    print("\noutput:", serialize(ans))
