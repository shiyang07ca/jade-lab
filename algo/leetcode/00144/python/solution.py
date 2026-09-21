from __future__ import annotations

# Created by shiyang07ca at 2024/02/11 00:03
# leetgo: dev
# https://leetcode.cn/problems/binary-tree-preorder-traversal/
from leetgo_py import TreeNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal1(self, root: TreeNode | None) -> list[int]:
        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        ans = []
        dfs(root)
        return ans

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        stk = [root]
        ans = []
        while stk:
            cur = stk.pop()
            ans.append(cur.val)
            if cur.right:
                stk.append(cur.right)
            if cur.left:
                stk.append(cur.left)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().preorderTraversal(root)

    print("\noutput:", serialize(ans))
