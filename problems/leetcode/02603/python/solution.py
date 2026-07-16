# Created by shiyang07ca at 2023/09/21 12:56
# leetgo: dev
# https://leetcode.cn/problems/collect-coins-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

# 相似题目
# LC310. 最小高度树 https://leetcode.cn/problems/minimum-height-trees


class Solution:
    # 链接：https://leetcode.cn/problems/collect-coins-in-a-tree/
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图
        deg = list(map(len, g))  # 每个节点的度数（邻居个数）

        left_edges = n - 1  # 剩余边数
        # 拓扑排序，去掉没有金币的子树
        q = []
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:  # 没有金币的叶子
                q.append(i)
        while q:
            left_edges -= 1  # 删除节点到其父节点的边
            for y in g[q.pop()]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:  # 没有金币的叶子
                    q.append(y)

        # 再次拓扑排序
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:  # 有金币的叶子（判断 c 是避免把没有金币的叶子也算进来）
                q.append(i)
        left_edges -= len(q)  # 删除所有叶子（到其父节点的边）
        for x in q:  # 遍历所有叶子
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:  # y 现在是叶子了
                    left_edges -= 1  # 删除 y（到其父节点的边）
        return max(left_edges * 2, 0)


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().collectTheCoins(coins, edges)

    print("\noutput:", serialize(ans))
