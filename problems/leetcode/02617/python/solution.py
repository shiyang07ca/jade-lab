# Created by shiyang07ca at 2024/03/22 07:32
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/solutions/
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1
        row, col = [[] for _ in range(m)], [[] for _ in range(n)]

        def update(x: int, y: int) -> int:
            return y if x == -1 or x > y else x

        for i in range(m):
            for j in range(n):
                while row[i] and row[i][0][1] + grid[i][row[i][0][1]] < j:
                    heapq.heappop(row[i])
                if row[i]:
                    dist[i][j] = update(dist[i][j], dist[i][row[i][0][1]] + 1)

                while col[j] and col[j][0][1] + grid[col[j][0][1]][j] < i:
                    heapq.heappop(col[j])
                if col[j]:
                    dist[i][j] = update(dist[i][j], dist[col[j][0][1]][j] + 1)

                if dist[i][j] != -1:
                    heapq.heappush(row[i], (dist[i][j], j))
                    heapq.heappush(col[j], (dist[i][j], i))

        return dist[m - 1][n - 1]


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumVisitedCells(grid)

    print("\noutput:", serialize(ans))
