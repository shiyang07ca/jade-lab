"""Kahn's topological sorting algorithm."""

from collections import deque
from collections.abc import Sequence


def topological_sort(vertex_count: int, edges: Sequence[tuple[int, int]]) -> list[int] | None:
    """Return a topological order, or ``None`` when the directed graph has a cycle."""
    if vertex_count < 0:
        raise ValueError("vertex_count must be non-negative")
    graph = [[] for _ in range(vertex_count)]
    indegree = [0] * vertex_count
    for source, target in edges:
        if not 0 <= source < vertex_count or not 0 <= target < vertex_count:
            raise IndexError("edge endpoint is outside the graph")
        graph[source].append(target)
        indegree[target] += 1
    queue = deque(vertex for vertex, degree in enumerate(indegree) if degree == 0)
    order: list[int] = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == vertex_count else None
