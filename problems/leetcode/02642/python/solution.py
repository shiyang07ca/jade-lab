# Created by shiyang07ca at 2024/03/26 22:31
# leetgo: dev
# https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Graph:
    # 链接：https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/solutions/2229013/dijkstra-suan-fa-mo-ban-pythonjavacgo-by-unmv/
    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[inf] * n for _ in range(n)]  # 邻接矩阵
        for x, y, w in edges:
            self.g[x][y] = w  # 添加一条边（题目保证没有重边）

    def addEdge(self, e: List[int]) -> None:
        self.g[e[0]][e[1]] = e[2]  # 添加一条边（题目保证这条边之前不存在）

    def shortestPath(self, start: int, end: int) -> int:
        n = len(self.g)
        dis = [inf] * n  # 从 start 出发，到各个点的最短路，如果不存在则为无穷大
        dis[start] = 0
        vis = [False] * n
        while True:  # 至多循环 n 次
            x = -1
            for i, (b, d) in enumerate(zip(vis, dis)):
                if not b and (x < 0 or d < dis[x]):
                    x = i
            if x < 0 or dis[x] == inf:  # 所有从 start 能到达的点都被更新了
                return -1  # 无法到达终点
            if x == end:  # 找到终点，提前退出
                return dis[x]
            vis[x] = True  # 标记，在后续的循环中无需反复更新 x 到其余点的最短路长度
            for y, w in enumerate(self.g[x]):
                if dis[x] + w < dis[y]:
                    dis[y] = dis[x] + w  # 更新最短路长度


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    edges: List[List[int]] = deserialize("List[List[int]]", constructor_params[1])
    obj = Graph(n, edges)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addEdge":
                method_params = split_array(params[i])
                edge: List[int] = deserialize("List[int]", method_params[0])
                obj.addEdge(edge)
                output.append("null")
            case "shortestPath":
                method_params = split_array(params[i])
                node1: int = deserialize("int", method_params[0])
                node2: int = deserialize("int", method_params[1])
                ans = serialize(obj.shortestPath(node1, node2))
                output.append(ans)

    print("\noutput:", join_array(output))
