# Created by shiyang07ca at 2024/02/16 13:18
# leetgo: dev
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        ans = []
        left = False
        while queue:
            t = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                t.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            ans.append(t[::-1] if left else t)
            left ^= 1

        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().zigzagLevelOrder(root)

    print("\noutput:", serialize(ans))
