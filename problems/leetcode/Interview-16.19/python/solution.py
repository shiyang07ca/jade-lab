# Created by shiyang07ca at 2023/06/22 08:08
# https://leetcode.cn/problems/pond-sizes-lcci/

"""
面试题 16.19. 水域大小 (Medium)
你有一个用于表示一片土地的整数矩阵 `land`，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水
域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所
有池塘的大小，返回值需要从小到大排序。

**示例：**

```
输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]

```

**提示：**

- `0 < len(land) <= 1000`
- `0 < len(land[i]) <= 1000`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: dfs, bfs


class Solution:
    # bfs
    def pondSizes1(self, land: List[List[int]]) -> List[int]:
        def bfs(i, j):
            if land[i][j] != 0:
                return 0

            cnt = 1
            q = deque([(i, j)])
            land[i][j] = 1
            while q:
                i, j = q.popleft()
                for a, b in dirs:
                    x, y = i + a, j + b
                    while 0 <= x < m and 0 <= y < n and land[x][y] == 0:
                        q.append((x, y))
                        land[x][y] = 1
                        cnt += 1
                        x, y = x + a, y + b
            return cnt

        ans = []
        m, n = len(land), len(land[0])
        dirs = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a != 0 or b != 0]
        for i in range(m):
            for j in range(n):
                if res := bfs(i, j):
                    ans.append(res)
        return sorted(ans)

    # dfs
    # 链接：https://leetcode.cn/problems/pond-sizes-lcci/solutions/2316704/mo-ban-wang-ge-tu-dfsfu-ti-dan-by-endles-p0n1/class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])

        def dfs(x: int, y: int) -> int:
            land[x][y] = 1  # 标记 (x,y) 被访问，避免重复访问
            cnt0 = 1
            # 访问八方向的 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < m and 0 <= j < n and land[i][j] == 0:
                        cnt0 += dfs(i, j)
            return cnt0

        ans = []
        for i, row in enumerate(land):
            for j, x in enumerate(row):
                if x == 0:  # 从没有访问过的 0 出发
                    ans.append(dfs(i, j))
        ans.sort()
        return ans


# @lc code=end

if __name__ == "__main__":
    land: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().pondSizes(land)

    print("\noutput:", serialize(ans))
