# Created by shiyang07ca at 2024/03/02 12:49
# leetgo: dev
# https://leetcode.cn/problems/reachable-nodes-with-restrictions/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reachableNodes1(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        restricted = set(restricted)

        ans = 0
        vis = set()

        def dfs(node):
            if node in vis or node in restricted:
                return

            nonlocal ans
            ans += 1
            vis.add(node)
            for c in g[node]:
                dfs(c)

        dfs(0)
        return ans

    # 链接：https://leetcode.cn/problems/reachable-nodes-with-restrictions/solutions/2662538/shu-shang-dfspythonjavacgojsrust-by-endl-0r3a/
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        r = set(restricted)
        g = [[] for _ in range(n)]
        for x, y in edges:
            if x not in r and y not in r:
                g[x].append(y)  # 都不受限才连边
                g[y].append(x)

        def dfs(x: int, fa: int) -> int:
            cnt = 1
            for y in g[x]:
                if y != fa:
                    cnt += dfs(y, x)
            return cnt

        return dfs(0, -1)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    restricted: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reachableNodes(n, edges, restricted)

    print("\noutput:", serialize(ans))
