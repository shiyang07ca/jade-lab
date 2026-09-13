from __future__ import annotations

from typing import cast

# Created by shiyang07ca at 2024/02/18 13:42
# leetgo: dev
# https://leetcode.cn/problems/n-ary-tree-preorder-traversal/
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
    def preorder(self, root: Node | None) -> list[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            for node in node.children:
                dfs(node)

        dfs(root)
        return ans


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: Node = cast(Node, deserialize("int", read_line()))
    ans = Solution().preorder(root)

    print("\noutput:", serialize(ans))
