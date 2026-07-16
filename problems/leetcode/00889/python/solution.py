# Created by shiyang07ca at 2024/02/22 00:01
# leetgo: dev
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

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
    def build(self, preorder, postorder, prel, prer, postl, postr):
        if prel > prer or postl > postr:
            return None

        # 注意
        if prel == prer:
            return TreeNode(preorder[prel])

        root_val = postorder[postr]
        root = TreeNode(root_val)
        # root_index = self.post_val_index[root_val]
        left_root_val = preorder[prel + 1]
        left_root_index = self.post_val_index[left_root_val]
        left_size = left_root_index - postl + 1

        root.left = self.build(
            preorder,
            postorder,
            prel + 1,
            prel + left_size,
            postl,
            left_root_index,
        )
        root.right = self.build(
            preorder,
            postorder,
            prel + left_size + 1,
            prer,
            left_root_index + 1,
            postr - 1,
        )

        return root

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        self.post_val_index = {}
        for i, val in enumerate(postorder):
            self.post_val_index[val] = i

        return self.build(
            preorder, postorder, 0, len(preorder) - 1, 0, len(postorder) - 1
        )


# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().constructFromPrePost(preorder, postorder)

    print("\noutput:", serialize(ans))
