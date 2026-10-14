# Created by shiyang07ca at 2026/10/15 00:20
# leetgo: 1.4.17
# https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/

from collections import deque
from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        start_row, start_col = entrance

        q = deque([(start_row, start_col, 0)])
        visited = set([(start_row, start_col)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            row, col, steps = q.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # 跳过越界的点
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                # 跳过已经访问过的位置和墙
                if (new_row, new_col) in visited or maze[new_row][new_col] == "+":
                    continue

                # 发现出口，距离一定是最小的
                if (
                    new_row == 0
                    or new_row == rows - 1
                    or new_col == 0
                    or new_col == cols - 1
                ):
                    return steps + 1

                # 入队时标记，避免重复访问
                visited.add((new_row, new_col))
                q.append((new_row, new_col, steps + 1))

        return -1


# @lc code=end

if __name__ == "__main__":
    maze: List[List[str]] = deserialize("List[List[str]]", read_line())
    entrance: List[int] = deserialize("List[int]", read_line())
    ans = Solution().nearestExit(maze, entrance)
    print("\noutput:", serialize(ans, "integer"))
