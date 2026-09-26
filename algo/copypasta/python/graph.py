"""Graph representation, breadth-first traversal, and Dijkstra's algorithm."""

from collections import deque
from collections.abc import Sequence
from heapq import heappop, heappush
from math import inf

WeightedGraph = list[list[tuple[int, int]]]


def adjacency_list(
    vertex_count: int,
    edges: Sequence[tuple[int, int, int]],
    *,
    directed: bool = False,
) -> WeightedGraph:
    """Build a weighted adjacency list from ``(from, to, weight)`` edges."""
    if vertex_count < 0:
        raise ValueError("vertex_count must be non-negative")
    graph: WeightedGraph = [[] for _ in range(vertex_count)]
    for source, target, weight in edges:
        if not 0 <= source < vertex_count or not 0 <= target < vertex_count:
            raise IndexError("edge endpoint is outside the graph")
        graph[source].append((target, weight))
        if not directed:
            graph[target].append((source, weight))
    return graph


"""
BFS 模板：
BFS使用队列，把每个还没有搜索到的点依次放入队列，然后再弹出队列的头部元素当做当前遍历点。

BFS总共有两个模板

模板一：
如果不需要确定当前遍历到了哪一层，BFS 模板如下。

while queue 不空：
    cur = queue.pop()
    if cur 有效且未被访问过：
        进行处理
    for 节点 in cur 的所有相邻节点：
        if 该节点有效：
            queue.push(该节点)

模板二：
如果要确定当前遍历到了哪一层，BFS 模板如下。
这里增加了 level 表示当前遍历到二叉树中的哪一层了，也可以理解为在一个图中，现在已经走了多少步了。size 表示在当前遍历层有多少个元素，也就是队列中的元素数，我们把这些元素一次性遍历完，即把当前层的所有元素都向外走了一步。

level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        if cur 有效且未被访问过：
            进行处理
        for 节点 in cur的所有相邻节点：
            if 该节点有效：
                queue.push(该节点)
    }
    level ++;

"""


def bfs_order(graph: Sequence[Sequence[int]], start: int) -> list[int]:
    """Return vertices reachable from ``start`` in breadth-first order."""
    if not 0 <= start < len(graph):
        raise IndexError("start is outside the graph")
    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([start])
    order: list[int] = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if not 0 <= neighbor < len(graph):
                raise IndexError("neighbor is outside the graph")
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return order


def dijkstra(
    graph: Sequence[Sequence[tuple[int, int]]], start: int
) -> list[int | float]:
    """Return shortest distances from ``start`` for a non-negative weighted graph."""
    if not 0 <= start < len(graph):
        raise IndexError("start is outside the graph")
    distances: list[int | float] = [inf] * len(graph)
    distances[start] = 0
    queue: list[tuple[int, int]] = [(0, start)]
    while queue:
        distance, vertex = heappop(queue)
        if distance != distances[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            if not 0 <= neighbor < len(graph):
                raise IndexError("neighbor is outside the graph")
            if weight < 0:
                raise ValueError("Dijkstra's algorithm requires non-negative weights")
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heappush(queue, (candidate, neighbor))
    return distances
