# Created by shiyang07ca at 2024/04/13 15:11
# leetgo: dev
# https://leetcode.cn/problems/find-champion-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for x, y in edges:
            g[x].append(y)
            indeg[y] += 1
        q = deque(i for i, v in enumerate(indeg) if v == 0)
        return q[0] if len(q) == 1 else -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findChampion(n, edges)
    print("\noutput:", serialize(ans, "integer"))
