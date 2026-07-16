# Created by shiyang07ca at 2024/02/23 00:01
# leetgo: dev
# https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/

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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        ans = []
        while q:
            t = 0
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                t += node.val
            ans.append(t)
        if len(ans) >= k:
            return sorted(ans)[-k]
        else:
            return -1


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestLevelSum(root, k)

    print("\noutput:", serialize(ans))
