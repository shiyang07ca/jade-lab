# Created by shiyang07ca at 2024/02/25 11:18
# leetgo: dev
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
    # 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/2652886/python3javacgotypescript-yi-ti-yi-jie-di-vley/
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while 1:
            if root.val < min(p.val, q.val):
                root = root.right
            elif root.val > max(p.val, q.val):
                root = root.left
            else:
                return root


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)

    print("\noutput:", serialize(ans))
