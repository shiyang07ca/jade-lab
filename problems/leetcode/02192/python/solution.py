# Created by shiyang07ca at 2024/04/05 23:50
# leetgo: dev
# https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 作者：灵茶山艾府
    # 链接：https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/solutions/2723203/liang-chong-fang-fa-ni-xiang-zheng-xiang-rwjs/
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[y].append(x)  # 反向建图

        def dfs(x: int) -> None:
            vis[x] = True  # 避免重复访问
            for y in g[x]:
                if not vis[y]:
                    dfs(y)  # 只递归没有访问过的点

        ans = [None] * n
        for i in range(n):
            vis = [False] * n
            dfs(i)  # 从 i 开始 DFS
            vis[i] = False  # ans[i] 不含 i
            ans[i] = [j for j, b in enumerate(vis) if b]
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getAncestors(n, edges)

    print("\noutput:", serialize(ans))
