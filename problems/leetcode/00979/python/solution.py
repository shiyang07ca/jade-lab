# Created by shiyang07ca at 2023/07/14 10:15
# leetgo: dev
# https://leetcode.cn/problems/distribute-coins-in-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 链接：https://leetcode.cn/problems/distribute-coins-in-binary-tree/solutions/2343262/tu-jie-mei-you-si-lu-jin-lai-miao-dong-p-vrni/
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return 0, 0
            coins_l, nodes_l = dfs(node.left)
            coins_r, nodes_r = dfs(node.right)
            coins = coins_l + coins_r + node.val  # 子树硬币个数
            nodes = nodes_l + nodes_r + 1  # 子树节点数
            nonlocal ans
            ans += abs(coins - nodes)
            return coins, nodes

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().distributeCoins(root)

    print("\noutput:", serialize(ans))
