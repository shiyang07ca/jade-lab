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


def dijkstra(graph: Sequence[Sequence[tuple[int, int]]], start: int) -> list[int | float]:
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
