# Created by shiyang07ca at 2024/04/05 23:42
# leetgo: dev
# https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/

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
    # 链接：https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/solutions/2232367/liang-chong-fang-fa-zi-ding-xiang-xia-zi-wj9v/
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], mn: int, mx: int) -> None:
            if node is None:
                return
            # 虽然题目要求「不同节点」，但是相同节点的差值为 0，不会影响最大差值
            # 所以先更新 mn 和 mx，再计算差值也是可以的
            # 在这种情况下，一定满足 mn <= node.val <= mx
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            nonlocal ans
            ans = max(ans, node.val - mn, mx - node.val)
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)

        dfs(root, root.val, root.val)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxAncestorDiff(root)

    print("\noutput:", serialize(ans))
