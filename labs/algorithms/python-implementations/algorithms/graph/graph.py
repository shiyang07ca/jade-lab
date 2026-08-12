"""

图

https://algo.itcharge.cn/08.Graph/01.Graph-Basic/02.Graph-Structure/

"""

"""

图的存储

- 邻接矩阵法
- 邻接表法
- 链式前向星

"""

# 邻接矩阵
from heapq import heappop, heappush
from math import inf
from typing import List, Tuple


class GraphAdjMat:
    # 图的初始化操作，ver_count 为顶点个数
    def __init__(self, ver_count):
        self.ver_count = ver_count  # 顶点个数
        self.adj_matrix = [
            [None for _ in range(ver_count)] for _ in range(ver_count)
        ]  # 邻接矩阵

    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count

    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)

    # 向图的邻接矩阵中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + " is not a valid vertex.")

        self.adj_matrix[vi][vj] = val

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + " is not a valid vertex.")

        return self.adj_matrix[vi][vj]

    # 根据邻接矩阵打印图的边
    def printGraph(self):
        for vi in range(self.ver_count):
            for vj in range(self.ver_count):
                val = self.get_edge(vi, vj)
                if val:
                    print(str(vi) + " - " + str(vj) + " : " + str(val))


# 邻接表
class EdgeNode:  # 边信息类
    def __init__(self, vj, val):
        self.vj = vj  # 边的终点
        self.val = val  # 边的权值
        self.next = None  # 下一条边


class VertexNode:  # 顶点信息类
    def __init__(self, vi):
        self.vi = vi  # 边的起点
        self.head = None  # 下一个邻接点


class GraphAdjList:
    def __init__(self, ver_count):
        self.ver_count = ver_count
        self.vertices = []
        for vi in range(ver_count):
            vertex = VertexNode(vi)
            self.vertices.append(vertex)

    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count

    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)

    # 向图的邻接表中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + " is not a valid vertex.")

        vertex = self.vertices[vi]
        edge = EdgeNode(vj, val)
        edge.next = vertex.head
        vertex.head = edge

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + " is not a valid vertex.")

        vertex = self.vertices[vi]
        cur_edge = vertex.head
        while cur_edge:
            if cur_edge.vj == vj:
                return cur_edge.val
            cur_edge = cur_edge.next
        return None

    # 根据邻接表打印图的边
    def printGraph(self):
        for vertex in self.vertices:
            cur_edge = vertex.head
            while cur_edge:
                print(
                    str(vertex.vi)
                    + " - "
                    + str(cur_edge.vj)
                    + " : "
                    + str(cur_edge.val)
                )
                cur_edge = cur_edge.next


# 链式前向星
class EdgeNodeLinked:  # 边信息类
    def __init__(self, vj, val):
        self.vj = vj  # 边的终点
        self.val = val  # 边的权值
        self.next = None  # 下一条边


class GraphLFStar:
    def __init__(self, ver_count, edge_count):
        self.ver_count = ver_count  # 顶点个数
        self.edge_count = edge_count  # 边个数
        self.head = [-1 for _ in range(ver_count)]  # 头节点数组
        self.edges = []  # 边集数组

    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count

    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for i in range(len(edges)):
            vi, vj, val = edges[i]
            self.add_edge(i, vi, vj, val)

            # 向图的边集数组中添加边：vi - vj，权值为 val

    def add_edge(self, index, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + " is not a valid vertex.")

        edge = EdgeNodeLinked(vj, val)  # 构造边节点
        edge.next = self.head[vi]  # 边节点的 next 指向原来首指针
        self.edges.append(edge)  # 边集数组添加该边
        self.head[vi] = index  # 首指针指向新加边所在边集数组的下标

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + " is not a valid vertex.")

        index = self.head[vi]  # 得到顶点 vi 相连的第一条边在边集数组的下标
        while index != -1:  # index == -1 时说明 vi 相连的边遍历完了
            if vj == self.edges[index].vj:  # 找到了 vi - vj 边
                return self.edges[index].val  # 返回 vi - vj 边的权值
            index = self.edges[index].next  # 取顶点 vi 相连的下一条边在边集数组的下标
        return None  # 没有找到 vi - vj 边

    # 根据链式前向星打印图的边
    def printGraph(self):
        for vi in range(self.ver_count):  # 遍历顶点 vi
            index = self.head[vi]  # 得到顶点 vi 相连的第一条边在边集数组的下标
            while index != -1:  # index == -1 时说明 vi 相连的边遍历完了
                print(
                    str(vi)
                    + " - "
                    + str(self.edges[index].vj)
                    + " : "
                    + str(self.edges[index].val)
                )
                index = self.edges[index].next  # 取顶点 vi 相连的下一条边在边集数组的下标


# 哈希表实现邻接表
class VertexNodeHash:  # 顶点信息类
    def __init__(self, vi):
        self.vi = vi  # 顶点
        self.adj_edges = dict()  # 顶点的邻接边


class GraphHashAdjList:
    def __init__(self):
        self.vertices = dict()  # 顶点

    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)

    # 向图中添加节点
    def add_vertex(self, vi):
        vertex = VertexNodeHash(vi)
        self.vertices[vi] = vertex

    # 向图的邻接表中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if vi not in self.vertices:
            self.add_vertex(vi)
        if vj not in self.vertices:
            self.add_vertex(vj)

        self.vertices[vi].adj_edges[vj] = val

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if vi in self.vertices and vj in self.vertices[vi].adj_edges:
            return self.vertices[vi].adj_edges[vj]
        return None

    # 根据邻接表打印图的边
    def printGraph(self):
        for vi in self.vertices:
            for vj in self.vertices[vi].adj_edges:
                print(
                    str(vi)
                    + " - "
                    + str(vj)
                    + " : "
                    + str(self.vertices[vi].adj_edges[vj])
                )


import unittest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.adj_mat_g = GraphAdjMat(5)
        self.adj_list_g = GraphAdjList(7)

    def testAdjMat(self):
        print("Graph Adjacency Matrix")
        edges = [
            [1, 2, 5],
            [2, 1, 5],
            [1, 3, 30],
            [3, 1, 30],
            [2, 3, 14],
            [3, 2, 14],
            [2, 4, 26],
            [4, 2, 26],
        ]
        self.adj_mat_g.creatGraph(edges)
        print(self.adj_mat_g.get_edge(3, 4))
        self.adj_mat_g.printGraph()

    def testAdjList(self):
        print("Grap Adjacency List")
        edges = [
            [1, 2, 5],
            [1, 5, 6],
            [2, 4, 7],
            [4, 3, 9],
            [3, 1, 2],
            [5, 6, 8],
            [6, 4, 3],
        ]
        self.adj_list_g.creatGraph(edges)
        print(self.adj_list_g.get_edge(3, 4))
        self.adj_list_g.printGraph()

    def testLFStar(self):
        print("GraphLFStar")
        graph = GraphLFStar(7, 7)
        edges = [
            [1, 2, 5],
            [1, 5, 6],
            [2, 4, 7],
            [4, 3, 9],
            [3, 1, 2],
            [5, 6, 8],
            [6, 4, 3],
        ]
        graph.creatGraph(edges)
        print(graph.get_edge(4, 3))
        print(graph.get_edge(4, 5))
        graph.printGraph()

    def testHashAdjList(self):
        print("HashAdjList")
        graph = GraphHashAdjList()
        edges = [
            [1, 2, 5],
            [1, 5, 6],
            [2, 4, 7],
            [4, 3, 9],
            [3, 1, 2],
            [5, 6, 8],
            [6, 4, 3],
        ]
        graph.creatGraph(edges)
        print(graph.get_edge(3, 4))
        graph.printGraph()


from collections import deque

"""
BFS

https://cp-algorithms.com/graph/breadth-first-search.html

应用
- 在一个无权图上求从起点到其他所有点的最短路径。

--------------------------------------------------------------------------------
    Breadth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                Q - Traversal Stack
--------------------------------------------------------------------------------
"""


def bfs(G, s):
    vis, Q = {s}, deque([s])
    print(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                print(v)
                vis.add(v)
                Q.append(v)


"""

单源最短路 Dijkstra

适用于稀疏图 O(mlogm)


模板题

LC743.网络延迟时间 https://leetcode-cn.com/problems/network-delay-time/

"""

# Dijkstra 算法模板
# 返回从 start 到每个点的最短路
def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
    dist = [inf] * len(g)
    dist[start] = 0
    h = [(0, start)]
    while h:
        d, x = heappop(h)
        if d > dist[x]:
            continue
        for y, wt in g[x]:
            new_d = dist[x] + wt
            if new_d < dist[y]:
                dist[y] = new_d
                heappush(h, (new_d, y))
    return dist


if __name__ == "__main__":
    unittest.main()
