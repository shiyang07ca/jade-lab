# Created by shiyang07ca at 2023/06/09 23:23
# https://leetcode.cn/problems/modify-graph-edge-weights/

"""
2699. 修改图中的边权 (Hard)
给你一个 `n` 个节点的 **无向带权连通** 图，节点编号为 `0` 到 `n - 1` ，再给你一个整数数组 `edges` ，
其中 `edges[i] = [aᵢ, bᵢ, wᵢ]` 表示节点 `aᵢ` 和 `bᵢ` 之间有一条边权为 `wᵢ` 的边。

部分边的边权为 `-1`（ `wᵢ = -1`），其他边的边权都为 **正** 数（ `wᵢ > 0`）。

你需要将所有边权为 `-1` 的边都修改为范围 `[1, 2 * 10⁹]` 中的 **正整数** ，使得从节点 `source` 到节点
`destination` 的 **最短距离** 为整数 `target` 。如果有 **多种** 修改方案可以使 `source` 和 `destinat
ion` 之间的最短距离等于 `target` ，你可以返回任意一种方案。

如果存在使 `source` 到 `destination` 最短距离为 `target` 的方案，请你按任意顺序返回包含所有边的数组
（包括未修改边权的边）。如果不存在这样的方案，请你返回一个 **空数组** 。

**注意：** 你不能修改一开始边权为正数的边。

**示例 1：**

**![](https://assets.leetcode.com/uploads/2023/04/18/graph.png)**

```
输入：n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
输出：[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
解释：上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。

```

**示例 2：**

**![](https://assets.leetcode.com/uploads/2023/04/18/graph-2.png)**

```
输入：n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
输出：[]
解释：上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个
空数组。

```

**示例 3：**

**![](https://assets.leetcode.com/uploads/2023/04/19/graph-3.png)**

```
输入：n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
输出：[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
解释：上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。

```

**提示：**

- `1 <= n <= 100`
- `1 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 3`
- `0 <= aᵢ, bᵢ < n`
- `wᵢ = -1` 或者 `1 <= wᵢ <= 10⁷`
- `aᵢ != bᵢ`
- `0 <= source, destination < n`
- `source != destination`
- `1 <= target <= 10⁹`
- 输入的图是连通图，且没有自环和重边。

"""

from typing import *
from leetgo_py import *

# @lc code=begin


# 链接：https://leetcode.cn/problems/modify-graph-edge-weights/solutions/2278296/xiang-xi-fen-xi-liang-ci-dijkstrachou-mi-gv1m/
class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for i, (x, y, _) in enumerate(edges):
            g[x].append((y, i))
            g[y].append((x, i))  # 建图，额外保存边的编号

        dis = [[inf, inf] for _ in range(n)]
        dis[source] = [0, 0]

        def dijkstra(k: int) -> None:  # 这里 k 表示第一次/第二次
            vis = [False] * n
            while True:
                # 找到当前最短路，去更新它的邻居的最短路
                # 根据数学归纳法，dis[x][k] 一定是最短路长度
                x = -1
                for y, (b, d) in enumerate(zip(vis, dis)):
                    if not b and (x < 0 or d[k] < dis[x][k]):
                        x = y
                if x == destination:  # 起点 source 到终点 destination 的最短路已确定
                    return
                vis[x] = True  # 标记，在后续的循环中无需反复更新 x 到其余点的最短路长度
                for y, eid in g[x]:
                    wt = edges[eid][2]
                    if wt == -1:
                        wt = 1  # -1 改成 1
                    if k == 1 and edges[eid][2] == -1:
                        # 第二次 Dijkstra，改成 w
                        w = delta + dis[y][0] - dis[x][1]
                        if w > wt:
                            edges[eid][2] = wt = w  # 直接在 edges 上修改
                    # 更新最短路
                    dis[y][k] = min(dis[y][k], dis[x][k] + wt)

        dijkstra(0)
        delta = target - dis[destination][0]
        if delta < 0:  # -1 全改为 1 时，最短路比 target 还大
            return []

        dijkstra(1)
        if dis[destination][1] < target:  # 最短路无法再变大，无法达到 target
            return []

        for e in edges:
            if e[2] == -1:  # 剩余没修改的边全部改成 1
                e[2] = 1
        return edges


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().modifiedGraphEdges(n, edges, source, destination, target)

    print("\noutput:", serialize(ans))
