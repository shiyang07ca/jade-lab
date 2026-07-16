# Created by shiyang07ca at 2023/09/06 00:19
# leetgo: dev
# https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/

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
    # 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/solutions/2428724/liang-chong-di-gui-si-lu-pythonjavacgojs-xxnk/
    def lcaDeepestLeaves1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1  # 全局最大深度

        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)  # 维护全局最大深度
                return depth
            left_max_depth = dfs(node.left, depth + 1)  # 获取左子树最深叶节点的深度
            right_max_depth = dfs(node.right, depth + 1)  # 获取右子树最深叶节点的深度
            if left_max_depth == right_max_depth == max_depth:
                ans = node
            return max(left_max_depth, right_max_depth)  # 当前子树最深叶节点的深度

        dfs(root, 0)
        return ans

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> (int, Optional[TreeNode]):
            if node is None:
                return 0, None
            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)
            if left_height > right_height:  # 左子树更高
                return left_height + 1, left_lca
            if left_height < right_height:  # 右子树更高
                return right_height + 1, right_lca
            return left_height + 1, node  # 一样高

        return dfs(root)[1]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().lcaDeepestLeaves(root)

    print("\noutput:", serialize(ans))
