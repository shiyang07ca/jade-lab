# Created by shiyang07ca at 2023/11/03 13:19
# leetgo: dev
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return

        queue = [root]
        while queue:
            q = queue[:]
            for _ in range(len(q)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            for a, b in pairwise(q):
                a.next = b

        return root


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().connect(root)

    print("\noutput:", serialize(ans))
