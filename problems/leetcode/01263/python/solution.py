# Created by shiyang07ca at 2023/05/08 21:42
# https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/

"""
1263. 推箱子 (Hard)
「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库
中的目标位置。

游戏地图用大小为 `m x n` 的网格 `grid` 表示，其中每个元素可
以是墙、地板或者是箱子。

现在你将作为玩家参与游戏，按规则将箱子 `'B'` 移动到目标位置
`'T'` ：

- 玩家用字符 `'S'` 表示，只要他在地板上，就可以在网格中向上
、下、左、右四个方向移动。
- 地板用字符 `'.'` 表示，意味着可以自由行走。
- 墙用字符 `'#'` 表示，意味着障碍物，不能通行。
- 箱子仅有一个，用字符 `'B'` 表示。相应地，网格上有一个目标
位置 `'T'`。
- 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子
会被移动到相邻的地板单元格。记作一次「推动」。
- 玩家无法越过箱子。

返回将箱子推到目标位置的最小 **推动** 次数，如果无法做到，请
返回 `-1`。

**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/upload
s/2019/11/16/sample_1_1620.png)**

```
输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#",".","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：3
解释：我们只需要返回推箱子的次数。
```

**示例 2：**

```
输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#","#","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：-1

```

**示例 3：**

```
输入：grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：5
解释：向下、向左、向左、向上再向上。

```

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 20`
- `grid` 仅包含字符 `'.'`, `'#'`,  `'S'` , `'T'`, 以及 `'B'`
。
- `grid` 中 `'S'`, `'B'` 和 `'T'` 各只能出现一个。

"""
from itertools import *
from collections import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: BFS


# 链接：https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/solutions/2261099/python3javacgotypescript-yi-ti-yi-jie-sh-xgcz/
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def f(i: int, j: int) -> int:
            return i * n + j

        def valid(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n and grid[i][j] != "#"

        # 找到盒子和人的初始位置
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "S":
                    si, sj = i, j
                elif c == "B":
                    bi, bj = i, j

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        g = deque([(f(si, sj), f(bi, bj), 0)])  # 三元组：人位置，箱子位置，当前移动j距离
        vis = [[False] * (m * n) for _ in range(m * n)]
        vis[f(si, sj)][f(bi, bj)] = True
        while g:
            # print(g)
            s, b, d = g.popleft()
            bi, bj = b // n, b % n
            if grid[bi][bj] == "T":
                return d
            si, sj = s // n, s % n
            for a, b in pairwise(dirs):
                sx, sy = si + a, sj + b  # 枚举玩家下一步位置
                if not valid(sx, sy):
                    continue
                if sx == bi and sy == bj:  # 如果玩家下一步位置和箱子重合，则可能推了箱子
                    bx, by = bi + a, bj + b
                    if not valid(bx, by) or vis[f(sx, sy)][f(bx, by)]:
                        continue
                    # 前进！
                    vis[f(sx, sy)][f(bx, by)] = True
                    g.append((f(sx, sy), f(bx, by), d + 1))  #  d+1, 进入下一层，加到队尾
                elif not vis[f(sx, sy)][f(bi, bj)]:
                    vis[f(sx, sy)][f(bi, bj)] = True
                    g.appendleft((f(sx, sy), f(bi, bj), d))  # d 不变，还在本层，加入队头

        return -1


# @lc code=end

if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().minPushBox(grid)
    print("output:", serialize(ans))
