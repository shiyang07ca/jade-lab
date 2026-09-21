from __future__ import annotations

# Created by shiyang07ca at 2024/02/20 00:02
# leetgo: dev
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from leetgo_py import TreeNode, deserialize, read_line, serialize

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
    def build(self, preorder, pl, pr, inorder, il, ir):
        if pl > pr or il > ir:
            return None

        root_val = preorder[pl]
        # 根节点在 inorder 中的位置
        root_index = self.inorder_val_index[root_val]
        root = TreeNode(root_val)
        # left_size = root_index - il == ineorder 中左树的长度
        left_size = root_index - il
        # preoder
        #    root          left                              right
        # |  pl  | pl+1  ....   pl + left_size  | pl + left_size + 1  .... pr |

        # inorder
        #       left                        root                  right
        # | il .......  root_index - 1 | root_index  | root_index + 1  ...... ir  |
        root.left = self.build(
            preorder, pl + 1, pl + left_size, inorder, il, root_index - 1
        )
        root.right = self.build(
            preorder, pl + left_size + 1, pr, inorder, root_index + 1, ir
        )

        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        self.inorder_val_index = {}
        for i, val in enumerate(inorder):
            self.inorder_val_index[val] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


# @lc code=end

if __name__ == "__main__":
    preorder: list[int] = deserialize("List[int]", read_line())
    inorder: list[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(preorder, inorder)

    print("\noutput:", serialize(ans))
