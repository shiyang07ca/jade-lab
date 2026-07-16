# Created by shiyang07ca at 2024/02/09 00:30
# leetgo: dev
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 分类讨论：
    # - 当前节点是空节点：返回当前节点
    # - 当前节点是 p：返回当前节点
    # - 当前节点是 q：返回当前节点
    # - 左右子树都能找到：返回当前节点
    # - 只有左子树找到：返回递归左子树结果
    # - 只有右子树找到：返回递归右子树结果
    # - 左右子树都没找到：返回空节点
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)

    print("\noutput:", serialize(ans))
