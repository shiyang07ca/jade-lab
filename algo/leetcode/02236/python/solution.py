from __future__ import annotations

# Created by shiyang07ca at 2023/08/20 00:08
# leetgo: dev
# https://leetcode.cn/problems/root-equals-sum-of-children/
from leetgo_py import TreeNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        if root is None or root.left is None or root.right is None:
            return False
        return root.val == (root.left.val + root.right.val)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().checkTree(root)

    print("\noutput:", serialize(ans))
