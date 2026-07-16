# Created by shiyang07ca at 2023/10/21 17:14
# leetgo: dev
# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countPairs1(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                # 路径压缩
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            p[pa] = pb
            size[pb] += size[pa]

        p = list(range(n))
        size = [1] * n
        ans = 0
        for a, b in edges:
            union(a, b)

        for i in range(n):
            ans += n - size[find(i)]

        return ans // 2

    # DFS
    # 链接：https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/solutions/
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        visited = [False] * n

        def dfs(x: int) -> int:
            visited[x] = True
            count = 1
            for y in g[x]:
                if not visited[y]:
                    count += dfs(y)
            return count

        res = 0
        for i in range(n):
            if not visited[i]:
                count = dfs(i)
                res += count * (n - count)
        return res // 2


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPairs(n, edges)

    print("\noutput:", serialize(ans))
