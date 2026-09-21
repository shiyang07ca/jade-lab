from __future__ import annotations

# Created by shiyang07ca at 2024/11/10 17:38
# leetgo: 1.4.10
# https://leetcode.cn/problems/construct-quad-tree/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(
        self,
        val: int,
        isLeaf: bool,
        topLeft: Node | None,
        topRight: Node | None,
        bottomLeft: Node | None,
        bottomRight: Node | None,
    ) -> None:
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# TODO:


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        def dfs(a, b, c, d):
            ok = True
            t = grid[a][b]
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    if grid[i][j] != t:
                        ok = False
                        break
            if ok:
                return Node(t, True, None, None, None, None)
            else:
                dx = c - a + 1
                dy = d - b + 1
                tl = dfs(a, b, a + dx // 2 - 1, b + dy // 2 - 1)
                tr = dfs(a, b + dy // 2, a + dx // 2 - 1, d)
                bl = dfs(a + dx // 2, b, c, b + dy // 2 - 1)
                br = dfs(a + dx // 2, b + dy // 2, c, d)
                return Node(0, False, tl, tr, bl, br)

        return dfs(0, 0, len(grid) - 1, len(grid) - 1)


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().construct(grid)
    print("\noutput:", serialize(ans, "integer[][]"))
