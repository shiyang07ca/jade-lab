# Created by shiyang07ca at 2023/12/07 00:06
# leetgo: dev
# https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minReorder1(self, n: int, connections: List[List[int]]) -> int:
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for x, y in connections:
            g1[x].append(y)
            g2[y].append(x)

        ans = 0
        q = deque([0])
        vis = {0}
        while q:
            u = q.popleft()
            for v in g1[u]:
                if v not in vis:
                    ans += 1
                    q.append(v)
                    vis.add(v)
            for v in g2[u]:
                if v not in vis:
                    q.append(v)
                    vis.add(v)
        return ans

    # 链接：https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/2328146/ke-neng-shi-shang-zui-tong-su-yi-dong-de-58by/
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(x: int, parent: int, e: List[List[List[int]]]) -> int:
            res = 0
            for a, c in e[x]:
                if a == parent:
                    continue
                res += c + dfs(a, x, e)
            return res

        e = [[] for _ in range(n)]
        for a, b in connections:
            e[a].append([b, 1])
            e[b].append([a, 0])

        return dfs(0, -1, e)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minReorder(n, connections)

    print("\noutput:", serialize(ans))
