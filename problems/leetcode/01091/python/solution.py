# Created by shiyang07ca at 2023/05/26 00:08
# https://leetcode.cn/problems/shortest-path-in-binary-matrix/

"""
1091. 二进制矩阵中的最短路径 (Medium)
给你一个 `n x n` 的二进制矩阵 `grid` 中，返回矩阵中最短 **畅通路径** 的长度。如果不存在这样的路径，
返回 `-1` 。

二进制矩阵中的 畅通路径 是一条从 **左上角** 单元格（即， `(0, 0)`）到 右下角 单元格（即， `(n - 1, n
- 1)`）的路径，该路径同时满足下述要求：

- 路径途经的所有单元格都的值都是 `0` 。
- 路径中所有相邻的单元格应当在 **8 个方向之一** 上连通（即，相邻两单元之间彼此不同且共享一条边或者一
个角）。

**畅通路径的长度** 是该路径途经的单元格总数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)

```
输入：grid = [[0,1],[1,0]]
输出：2

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)

```
输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4

```

**示例 3：**

```
输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1

```

**提示：**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` 为 `0` 或 `1`

"""
from collections import *
from itertools import *


from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        if len(grid) == 1:
            return 1

        q = deque([(0, 0)])
        n = len(grid)
        ans = 1
        vis = set()
        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in product([-1, 0, 1], repeat=2):
                    u, v = i + a, j + b
                    if (
                        (u, v) not in vis
                        and u >= 0
                        and u < n
                        and v >= 0
                        and v < n
                        and grid[u][v] == 0
                        and (a != 0 or b != 0)
                    ):
                        if u == v == n - 1:
                            return ans
                        vis.add((u, v))
                        q.append((u, v))
        return -1


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestPathBinaryMatrix(grid)

    print("\noutput:", serialize(ans))
