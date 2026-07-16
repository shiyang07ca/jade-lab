# Created by shiyang07ca at 2023/05/30 10:19
# https://leetcode.cn/problems/delete-nodes-and-return-forest/

"""
1110. 删点成林 (Medium)
给出二叉树的根节点 `root`，树上每个节点都有一个不同的值。

如果节点值在 `to_delete` 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集
合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/07/05/screen-shot-2019-07-01-at-5
3836-pm.png)**

```
输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

```

**示例 2：**

```
输入：root = [1,2,4,null,3], to_delete = [3]
输出：[[1,2,4]]

```

**提示：**

- 树中的节点数最大为 `1000`。
- 每个节点都有一个介于 `1` 到 `1000` 之间的值，且各不相同。
- `to_delete.length <= 1000`
- `to_delete` 包含一些从 `1` 到 `1000`、各不相同的值。

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# TODO:
# tag: binary tree


# 链接：https://leetcode.cn/problems/delete-nodes-and-return-forest/solutions/2289131/he-shi-ji-lu-da-an-pythonjavacgo-by-endl-lpcd/
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        ans = []
        s = set(to_delete)

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val not in s:
                return node
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            return None

        if dfs(root):
            ans.append(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    to_delete: List[int] = deserialize("List[int]", read_line())
    ans = Solution().delNodes(root, to_delete)

    print("\noutput:", serialize(ans))
