# Created by shiyang07ca at 2023/12/15 22:16
# leetgo: dev
# https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/

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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q, level = [root], 0
        while q[0].left:
            q = list(chain.from_iterable((node.left, node.right) for node in q))
            # print([n.val for n in q])
            if level == 0:
                for i in range(len(q) // 2):
                    x, y = q[i], q[len(q) - 1 - i]
                    x.val, y.val = y.val, x.val
            level ^= 1
        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().reverseOddLevels(root)

    print("\noutput:", serialize(ans))
