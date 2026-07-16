# Created by shiyang07ca at 2024/02/12 01:28
# leetgo: dev
# https://leetcode.cn/problems/binary-tree-postorder-traversal/

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
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            ans.append(node.val)

        ans = []
        dfs(root)
        return ans

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack1, stack2 = [root], []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)

        ans = []
        while stack2:
            ans.append(stack2.pop().val)

        return ans

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        h = root
        c = None
        stack = [h]
        while stack:
            c = stack[-1]
            if c.left and h != c.left and h != c.right:
                stack.append(c.left)
            elif c.right and h != c.right:
                stack.append(c.right)
            else:
                ans.append(stack.pop().val)
                h = c

        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().postorderTraversal(root)

    print("\noutput:", serialize(ans))
