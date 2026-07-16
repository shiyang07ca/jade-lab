# Created by shiyang07ca at 2024/04/03 23:18
# leetgo: dev
# https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def dfs(node):
            if not node:
                return
            if node.val == target.val:
                return node
            return dfs(node.left) or dfs(node.right)

        return dfs(cloned)


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    tree: TreeNode = deserialize("TreeNode", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().getTargetCopy(tree, target)

    print("\noutput:", serialize(ans))
