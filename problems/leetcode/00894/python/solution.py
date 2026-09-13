from __future__ import annotations

from functools import cache

# Created by shiyang07ca at 2024/04/02 09:27
# leetgo: dev
# https://leetcode.cn/problems/all-possible-full-binary-trees/
from leetgo_py import TreeNode, deserialize, read_line, serialize

# @lc code=begin

# TODO:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 链接：https://leetcode.cn/problems/all-possible-full-binary-trees/solutions/2719981/dong-tai-gui-hua-pythonjavacgojsrust-by-u3waz/
MX = 11
f = [[] for _ in range(MX)]
f[1] = [TreeNode()]
for i in range(2, MX):  # 计算 f[i]
    f[i] = [
        TreeNode(0, left, right)
        for j in range(1, i)  # 枚举左子树叶子数
        for left in f[j]  #  枚举左子树
        for right in f[i - j]
    ]  # 枚举右子树


class Solution:
    def allPossibleFBT1(self, n: int) -> list[TreeNode | None]:
        return f[(n + 1) // 2] if n % 2 else []

    # 链接：https://leetcode.cn/problems/all-possible-full-binary-trees/solutions/2720015/python3javacgotypescript-yi-ti-yi-jie-ji-d1vm/
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        @cache
        def dfs(n: int) -> list[TreeNode | None]:
            if n == 1:
                return [TreeNode()]
            ans = []
            for i in range(n - 1):
                j = n - 1 - i
                for left in dfs(i):
                    for right in dfs(j):
                        ans.append(TreeNode(0, left, right))
            return ans

        return dfs(n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().allPossibleFBT(n)

    print("\noutput:", serialize(ans))
