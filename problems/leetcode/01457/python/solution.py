# Created by shiyang07ca at 2023/11/25 22:43
# leetgo: dev
# https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def pseudoPalindromicPaths1(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pre):
            if not node.left and not node.right:
                nonlocal ans
                ans += 1 if pre.bit_count() <= 1 else 0
                return

            if node.left:
                dfs(node.left, pre ^ (1 << (node.left.val - 1)))
            if node.right:
                dfs(node.right, pre ^ (1 << (node.right.val - 1)))

        ans = 0
        dfs(root, (1 << (root.val - 1)))
        return ans

    # 链接：https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/
    def pseudoPalindromicPaths(self, root: Optional[TreeNode], mask=0) -> int:
        if root is None:
            return 0
        mask ^= 1 << root.val  # 修改 root.val 出现次数的奇偶性
        if root.left is root.right:  # root 是叶子节点
            return 1 if mask & (mask - 1) == 0 else 0
        return self.pseudoPalindromicPaths(
            root.left, mask
        ) + self.pseudoPalindromicPaths(root.right, mask)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().pseudoPalindromicPaths(root)

    print("\noutput:", serialize(ans))
