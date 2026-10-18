from __future__ import annotations

from typing import cast

# Created by shiyang07ca at 2024/02/09 00:30
# leetgo: dev
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
from leetgo_py import TreeNode, deserialize, read_line, serialize

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        def dfs(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return None

            # 找到目标，向上返回。
            if node is p or node is q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            # 两边各有一个目标，当前节点就是最近公共祖先。
            if left is not None and right is not None:
                return node

            # 只有一边有结果就原样返回；都没有则返回 None。
            if left is not None:
                return left
            return right

        return dfs(root)


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: TreeNode = cast(TreeNode, deserialize("int", read_line()))
    q: TreeNode = cast(TreeNode, deserialize("int", read_line()))
    ans = Solution().lowestCommonAncestor(root, p, q)

    print("\noutput:", serialize(ans))
