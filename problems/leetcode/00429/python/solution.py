from __future__ import annotations

from typing import cast

# Created by shiyang07ca at 2024/02/17 00:05
# leetgo: dev
# https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val: int = 0, children: list[Node] | None = None) -> None:
        self.val = val
        self.children = [] if children is None else children


class Solution:
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        if root is None:
            return []

        queue = [root]
        ans = []
        while queue:
            t = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                t.append(cur.val)
                for node in cur.children:
                    queue.append(node)
            ans.append(t)
        return ans


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: Node = cast(Node, deserialize("int", read_line()))
    ans = Solution().levelOrder(root)

    print("\noutput:", serialize(ans))
