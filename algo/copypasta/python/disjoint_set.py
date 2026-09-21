"""Disjoint-set union with path compression and union by size."""


class DisjointSet:
    """Maintain components for integer elements in ``range(size)``."""

    def __init__(self, size: int) -> None:
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be non-negative")
        self._parent = list(range(size))
        self._sizes = [1] * size
        self._components = size

    def __len__(self) -> int:
        return len(self._parent)

    @property
    def components(self) -> int:
        return self._components

    def _validate(self, element: int) -> None:
        if not isinstance(element, int) or isinstance(element, bool):
            raise TypeError("element must be an integer")
        if not 0 <= element < len(self):
            raise IndexError("element is outside this disjoint set")

    def find(self, element: int) -> int:
        self._validate(element)
        root = element
        while root != self._parent[root]:
            root = self._parent[root]
        while element != root:
            parent = self._parent[element]
            self._parent[element] = root
            element = parent
        return root

    def union(self, left: int, right: int) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self._sizes[left_root] < self._sizes[right_root]:
            left_root, right_root = right_root, left_root
        self._parent[right_root] = left_root
        self._sizes[left_root] += self._sizes[right_root]
        self._components -= 1
        return True

    def connected(self, left: int, right: int) -> bool:
        return self.find(left) == self.find(right)

    def component_size(self, element: int) -> int:
        return self._sizes[self.find(element)]
