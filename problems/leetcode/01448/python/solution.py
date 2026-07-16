# Created by shiyang07ca at 2023/08/25 00:12
# leetgo: dev
# https://leetcode.cn/problems/count-good-nodes-in-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(n, m):
            nonlocal ans
            if n.val >= m:
                ans += 1
                if n.left:
                    dfs(n.left, n.val)
                if n.right:
                    dfs(n.right, n.val)
            else:
                if n.left:
                    dfs(n.left, m)
                if n.right:
                    dfs(n.right, m)

        dfs(root, root.val)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().goodNodes(root)

    print("\noutput:", serialize(ans))
