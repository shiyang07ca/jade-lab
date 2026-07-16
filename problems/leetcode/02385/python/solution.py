# Created by shiyang07ca at 2024/04/24 00:02
# leetgo: dev
# https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/

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
    # 链接：https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/solutions/2753470/cong-liang-ci-bian-li-dao-yi-ci-bian-li-tmt0x/
    def amountOfTime1(self, root: Optional[TreeNode], start: int) -> int:
        fa = {}
        start_node = None

        def dfs(node: Optional[TreeNode], from_: Optional[TreeNode]) -> None:
            if node is None:
                return
            fa[node] = from_  # 记录每个节点的父节点
            if node.val == start:  # 找到 start
                nonlocal start_node
                start_node = node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        def maxDepth(node: Optional[TreeNode], from_: TreeNode) -> int:
            if node is None:
                return -1  # 注意这里是 -1，因为 start 的深度为 0
            return (
                max(
                    maxDepth(x, node)
                    for x in (node.left, node.right, fa[node])
                    if x != from_
                )
                + 1
            )

        return maxDepth(start_node, start_node)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> (int, bool):
            if node is None:
                return 0, False
            l_len, l_found = dfs(node.left)
            r_len, r_found = dfs(node.right)
            nonlocal ans
            if node.val == start:
                # 计算子树 start 的最大深度
                # 注意这里和方法一的区别，max 后面没有 +1，所以算出的也是最大深度
                ans = max(l_len, r_len)
                return 1, True  # 找到了 start
            if l_found or r_found:
                # 只有在左子树或右子树包含 start 时，才能更新答案
                ans = max(ans, l_len + r_len)  # 两条链拼成直径
                # 保证 start 是直径端点
                return (l_len if l_found else r_len) + 1, True
            return max(l_len, r_len) + 1, False

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().amountOfTime(root, start)
    print("\noutput:", serialize(ans, "integer"))
