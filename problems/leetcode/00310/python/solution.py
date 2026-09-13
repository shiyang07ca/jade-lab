from __future__ import annotations

from collections import deque

# Created by shiyang07ca at 2024/03/17 11:24
# leetgo: dev
# https://leetcode.cn/problems/minimum-height-trees/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-height-trees/solutions/2691752/python3javacgotypescript-yi-ti-yi-jie-tu-4aet/
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            degree[a] += 1
            degree[b] += 1
        q = deque(i for i in range(n) if degree[i] == 1)
        ans = []
        while q:
            ans.clear()
            for _ in range(len(q)):
                a = q.popleft()
                ans.append(a)
                for b in g[a]:
                    degree[b] -= 1
                    if degree[b] == 1:
                        q.append(b)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMinHeightTrees(n, edges)

    print("\noutput:", serialize(ans))
