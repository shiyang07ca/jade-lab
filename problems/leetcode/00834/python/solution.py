# Created by shiyang07ca at 2023/07/16 22:17
# leetgo: dev
# https://leetcode.cn/problems/sum-of-distances-in-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


# 链接：https://leetcode.cn/problems/sum-of-distances-in-tree/solutions/2345592/tu-jie-yi-zhang-tu-miao-dong-huan-gen-dp-6bgb/
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]  # g[x] 表示 x 的所有邻居
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = [0] * n
        size = [1] * n  # 注意这里初始化成 1 了，下面只需要累加儿子的子树大小

        def dfs(x: int, fa: int, depth: int) -> None:
            ans[0] += depth  # depth 为 0 到 x 的距离
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    dfs(y, x, depth + 1)  # x 是 y 的父节点
                    size[x] += size[y]  # 累加 x 的儿子 y 的子树大小

        dfs(0, -1, 0)  # 0 没有父节点

        def reroot(x: int, fa: int) -> None:
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    ans[y] = ans[x] + n - 2 * size[y]
                    reroot(y, x)  # x 是 y 的父节点

        reroot(0, -1)  # 0 没有父节点
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sumOfDistancesInTree(n, edges)

    print("\noutput:", serialize(ans))
