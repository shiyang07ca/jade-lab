# Created by shiyang07ca at 2023/09/18 00:00
# leetgo: dev
# https://leetcode.cn/problems/house-robber-iii/

from functools import cache

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
    # 链接：https://leetcode.cn/problems/house-robber-iii/description/
    def rob1(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:  # 递归边界
                return 0, 0  # 没有节点，怎么选都是 0
            l_rob, l_not_rob = dfs(node.left)  # 递归左子树
            r_rob, r_not_rob = dfs(node.right)  # 递归右子树
            rob = l_not_rob + r_not_rob + node.val  # 选
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)  # 不选
            return rob, not_rob

        return max(dfs(root))  # 根节点选或不选的最大值

    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val
        elif root.left is None:
            return max(
                root.val + self.rob(root.right.left) + self.rob(root.right.right),
                self.rob(root.right),
            )
        elif root.right is None:
            return max(
                root.val + self.rob(root.left.left) + self.rob(root.left.right),
                self.rob(root.left),
            )
        l = self.rob(root.left)
        r = self.rob(root.right)

        return max(
            l + r,
            root.val
            + self.rob(root.left.left)
            + self.rob(root.left.right)
            + self.rob(root.right.left)
            + self.rob(root.right.right),
        )


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().rob(root)

    print("\noutput:", serialize(ans))
