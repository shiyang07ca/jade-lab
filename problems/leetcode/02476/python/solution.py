# Created by shiyang07ca at 2024/02/24 12:42
# leetgo: dev
# https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/

from bisect import *
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
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        vals = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        n = len(vals)
        ans = []
        for q in queries:
            mi = bisect_right(vals, q)
            ma = bisect_left(vals, q)
            ans.append(
                [
                    vals[mi - 1] if 0 < mi <= n and vals[mi - 1] <= q else -1,
                    vals[ma] if ma < n else -1,
                ]
            )
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().closestNodes(root, queries)

    print("\noutput:", serialize(ans))
