# Created by shiyang07ca at 2026/09/20 23:34
# leetgo: 1.4.17
# https://leetcode.cn/problems/evaluate-division/

from typing import *

from leetgo_py import *

# @lc code=begin


# TODO
# tag: Disjoint Set
class WeightedUnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

        # 唯一需要记住的权值定义：
        # ratio_to_parent[x] = x / parent[x]
        # 根节点的父节点是自己，所以根节点的权值为 1。
        self.ratio_to_parent = [1.0] * n

    def find(self, node: int) -> int:
        """返回 node 的根节点，并把 node 到根路径上的权值合并起来。"""
        parent = self.parent[node]
        if parent == node:
            return node

        root = self.find(parent)

        # 递归返回后：
        # ratio_to_parent[parent] = parent / root
        # 原来 ratio_to_parent[node] = node / parent
        # 两者相乘得到 node / root。
        self.ratio_to_parent[node] *= self.ratio_to_parent[parent]
        self.parent[node] = root
        return root

    def union(self, numerator: int, denominator: int, quotient: float) -> None:
        """加入 numerator / denominator = quotient 这条已知关系。"""
        numerator_root = self.find(numerator)
        denominator_root = self.find(denominator)
        if numerator_root == denominator_root:
            return

        # find 后有：
        # numerator / numerator_root = ratio_to_parent[numerator]
        # denominator / denominator_root = ratio_to_parent[denominator]
        # 现在把 numerator_root 接到 denominator_root 下，需要保存：
        # numerator_root / denominator_root
        self.parent[numerator_root] = denominator_root
        self.ratio_to_parent[numerator_root] = (
            quotient
            * self.ratio_to_parent[denominator]
            / self.ratio_to_parent[numerator]
        )

    def divide(self, numerator: int, denominator: int) -> Optional[float]:
        """返回 numerator / denominator；没有关系时返回 None。"""
        if self.find(numerator) != self.find(denominator):
            return None

        # 两个变量指向同一个根，因此根可以约掉：
        # numerator / denominator
        # = (numerator / root) / (denominator / root)
        return self.ratio_to_parent[numerator] / self.ratio_to_parent[denominator]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # 列表只能用整数下标，因此先把变量名映射为连续整数。
        variable_to_id: Dict[str, int] = {}
        for equation in equations:
            for variable in equation:
                if variable not in variable_to_id:
                    variable_to_id[variable] = len(variable_to_id)

        union_find = WeightedUnionFind(len(variable_to_id))
        for (numerator, denominator), quotient in zip(equations, values, strict=True):
            union_find.union(
                variable_to_id[numerator],
                variable_to_id[denominator],
                quotient,
            )

        answers = []
        for numerator, denominator in queries:
            if numerator not in variable_to_id or denominator not in variable_to_id:
                answers.append(-1.0)
                continue

            quotient = union_find.divide(
                variable_to_id[numerator], variable_to_id[denominator]
            )
            answers.append(quotient if quotient is not None else -1.0)

        return answers


# @lc code=end

if __name__ == "__main__":
    equations: List[List[str]] = deserialize("List[List[str]]", read_line())
    values: List[float] = deserialize("List[float]", read_line())
    queries: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().calcEquation(equations, values, queries)
    print("\noutput:", serialize(ans, "double[]"))
