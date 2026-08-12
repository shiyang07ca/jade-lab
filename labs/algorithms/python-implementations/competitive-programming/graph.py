"""Kahn's algorithm for topological sorting.

References:
https://oi-wiki.org/graph/topo/
https://cp-algorithms.com/graph/topological-sort.html
"""

from collections import deque
from collections.abc import Sequence


def top_sort(n: int, edges: Sequence[tuple[int, int]]) -> list[int] | None:
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for x, y in edges:
        g[x - 1].append(y - 1)
        indeg[y - 1] += 1
    order = []  # 拓扑序
    q = deque(i for i, v in enumerate(indeg) if v == 0)
    while q:  # BFS，每个点当入度为 0 时放入拓扑序结果中
        x = q.popleft()
        order.append(x)
        for y in g[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return order if len(order) == n else None
