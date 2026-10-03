"""并查集：路径压缩 + 按大小合并，单次操作均摊 O(alpha(n))，空间 O(n)。"""


class UnionFind:
    """维护编号为 0 到 n-1 的元素，调用方保证下标合法。"""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n  # 只有根节点的 size 表示当前连通块大小
        self.groups = n  # 连通块数量

    def find(self, x: int) -> int:
        """查找代表元，并将路径上的节点直接连到根节点。"""
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x: int, y: int) -> bool:
        """按大小合并；已经连通时返回 False，否则返回 True。"""
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.groups -= 1
        return True

    def same(self, x: int, y: int) -> bool:
        """判断两个元素是否连通。"""
        return self.find(x) == self.find(y)
