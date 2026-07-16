# Created by shiyang07ca at 2023/12/04 22:34
# leetgo: dev
# https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 链接：https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0

        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            dfs(node.right)  # 递归右子树
            # 递归结束后，s 就等于右子树的所有节点值之和
            nonlocal s
            s += node.val
            node.val = s  # 此时 s 就是 >= node.val 的所有数之和
            dfs(node.left)  # 递归左子树

        dfs(root)
        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().bstToGst(root)

    print("\noutput:", serialize(ans))
