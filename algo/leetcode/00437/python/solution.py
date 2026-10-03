# Created by shiyang07ca at 2026/10/03 13:44
# leetgo: 1.4.17
# https://leetcode.cn/problems/path-sum-iii/

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 当前节点的祖先链上，每个前缀和出现的次数，0 表示根节点之前的空路径。
        prefix_counts = {0: 1}

        # 返回以 node 为根的子树中，符合条件的路径总数。
        def dfs(node: Optional[TreeNode], parent_sum: int) -> int:
            if node is None:
                return 0

            # 1. 计算根到当前节点的前缀和。
            current_sum = parent_sum + node.val

            # 2. 统计以当前节点为终点的合法路径。
            # 路径和 = 当前前缀和 - 路径起点之前的前缀和。
            required_prefix_sum = current_sum - targetSum
            paths_ending_here = prefix_counts.get(required_prefix_sum, 0)

            # 3. 加入当前前缀和，供子节点使用。
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

            # 4. 统计左右子树中的合法路径。
            paths_in_children = dfs(node.left, current_sum)
            paths_in_children += dfs(node.right, current_sum)

            # 5. 撤销当前前缀和，避免影响兄弟分支。
            prefix_counts[current_sum] -= 1
            if prefix_counts[current_sum] == 0:
                del prefix_counts[current_sum]

            return paths_ending_here + paths_in_children

        return dfs(root, 0)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().pathSum(root, targetSum)
    print("\noutput:", serialize(ans, "integer"))
