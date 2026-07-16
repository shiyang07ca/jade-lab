# Created by shiyang07ca at 2024/02/26 00:00
# leetgo: dev
# https://leetcode.cn/problems/range-sum-of-bst/

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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if low <= node.val <= high:
                nonlocal ans
                ans += node.val
            dfs(node.right)

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().rangeSumBST(root, low, high)

    print("\noutput:", serialize(ans))
