# Created by shiyang07ca at 2026/10/04 16:13
# leetgo: 1.4.17
# https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/

from functools import cache
from typing import *

from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        @cache
        def dfs(node: TreeNode | None, direction: str) -> int:
            # 从 node 出发，第一步必须朝 direction 走。
            if node is None:
                return 0

            if direction == "left" and node.left is not None:
                return 1 + dfs(node.left, "right")

            if direction == "right" and node.right is not None:
                return 1 + dfs(node.right, "left")

            return 0

        def visit(node: TreeNode | None) -> int:
            if node is None:
                return 0

            # 起点是当前节点。
            starting_here = max(
                dfs(node, "left"),
                dfs(node, "right"),
            )

            # 起点也可能在左子树或右子树中的任意位置。
            return max(
                starting_here,
                visit(node.left),
                visit(node.right),
            )

        return visit(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().longestZigZag(root)
    print("\noutput:", serialize(ans, "integer"))
