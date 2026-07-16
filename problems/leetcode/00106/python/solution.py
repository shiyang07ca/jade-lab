# Created by shiyang07ca at 2024/02/21 00:02
# leetgo: dev
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# template

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def build(self, postorder, pl, pr, inorder, il, ir):
        if pl > pr or il > ir:
            return None

        root_val = postorder[pr]
        root_index = self.inorder_val_index[root_val]
        root = TreeNode(root_val)
        left_size = root_index - il
        root.left = self.build(
            postorder, pl, pl + left_size - 1, inorder, il, root_index - 1
        )
        root.right = self.build(
            postorder, pl + left_size, pr - 1, inorder, root_index + 1, ir
        )

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder_val_index = {}
        for i, val in enumerate(inorder):
            self.inorder_val_index[val] = i

        return self.build(
            postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1
        )


# @lc code=end

if __name__ == "__main__":
    inorder: List[int] = deserialize("List[int]", read_line())
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(inorder, postorder)

    print("\noutput:", serialize(ans))
