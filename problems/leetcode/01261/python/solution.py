# Created by shiyang07ca at 2024/03/12 00:17
# leetgo: dev
# https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.set = set()

        def dfs(node):
            if not node:
                return
            self.set.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)

        root.val = 0
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    root: TreeNode = deserialize("TreeNode", constructor_params[0])
    obj = FindElements(root)

    for i in range(1, len(ops)):
        match ops[i]:
            case "find":
                method_params = split_array(params[i])
                target: int = deserialize("int", method_params[0])
                ans = serialize(obj.find(target))
                output.append(ans)

    print("\noutput:", join_array(output))
