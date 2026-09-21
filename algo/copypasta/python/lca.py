"""Binary lifting for lowest common ancestor queries."""

from collections.abc import Sequence


class LowestCommonAncestor:
    """Preprocess a connected undirected tree for O(log n) queries."""

    def __init__(
        self, vertex_count: int, edges: Sequence[tuple[int, int]], *, root: int = 0
    ) -> None:
        if vertex_count <= 0:
            raise ValueError("vertex_count must be positive")
        if not 0 <= root < vertex_count:
            raise IndexError("root is outside the tree")
        if len(edges) != vertex_count - 1:
            raise ValueError("a tree must contain vertex_count - 1 edges")
        graph = [[] for _ in range(vertex_count)]
        for left, right in edges:
            if not 0 <= left < vertex_count or not 0 <= right < vertex_count:
                raise IndexError("edge endpoint is outside the tree")
            graph[left].append(right)
            graph[right].append(left)

        levels = vertex_count.bit_length()
        parents = [[-1] * levels for _ in range(vertex_count)]
        depths = [-1] * vertex_count
        depths[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            for neighbor in graph[vertex]:
                if neighbor == parents[vertex][0]:
                    continue
                if depths[neighbor] != -1:
                    raise ValueError("edges contain a cycle")
                parents[neighbor][0] = vertex
                depths[neighbor] = depths[vertex] + 1
                stack.append(neighbor)
        if any(depth == -1 for depth in depths):
            raise ValueError("tree must be connected")
        for level in range(1, levels):
            for vertex in range(vertex_count):
                parent = parents[vertex][level - 1]
                if parent != -1:
                    parents[vertex][level] = parents[parent][level - 1]
        self._parents = parents
        self._depths = depths

    def _validate(self, vertex: int) -> None:
        if not 0 <= vertex < len(self._parents):
            raise IndexError("vertex is outside the tree")

    def kth_ancestor(self, vertex: int, distance: int) -> int | None:
        self._validate(vertex)
        if distance < 0:
            raise ValueError("distance must be non-negative")
        if distance > self._depths[vertex]:
            return None
        for level in range(distance.bit_length()):
            if distance & (1 << level):
                vertex = self._parents[vertex][level]
        return vertex

    def query(self, left: int, right: int) -> int:
        self._validate(left)
        self._validate(right)
        if self._depths[left] > self._depths[right]:
            left, right = right, left
        ancestor = self.kth_ancestor(right, self._depths[right] - self._depths[left])
        if ancestor is None:
            raise AssertionError("validated tree produced no ancestor")
        right = ancestor
        if left == right:
            return left
        for level in range(len(self._parents[left]) - 1, -1, -1):
            if self._parents[left][level] != self._parents[right][level]:
                left = self._parents[left][level]
                right = self._parents[right][level]
        return self._parents[left][0]
