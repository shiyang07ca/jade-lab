# Created by shiyang07ca at 2023/06/12 00:02
# https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/

"""
1483. 树节点的第 K 个祖先 (Hard)
给你一棵树，树上有 `n` 个节点，按从 `0` 到 `n-1` 编号。树以父节点数组的形式给出，其中 `parent[i]` 是
节点 `i` 的父节点。树的根节点是编号为 `0` 的节点。

树节点的第 `k`个祖先节点是从该节点到根节点路径上的第 `k` 个节点。

实现 `TreeAncestor` 类：

- `TreeAncestor（int n， int[] parent）` 对树和父数组中的节点数初始化对象。
- `getKthAncestor` `(int node, int k)` 返回节点 `node` 的第 `k` 个祖先节点。如果不存在这样的祖先节点
，返回 `-1` 。

**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/14/1528_ex1.png)**

```
输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点

```

**提示：**

- `1 <= k <= n <= 5 * 10⁴`
- `parent[0] == -1` 表示编号为 `0` 的节点是根节点。
- 对于所有的 `0 < i < n` ， `0 <= parent[i] < n` 总成立
- `0 <= node < n`
- 至多查询 `5 * 10⁴` 次

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: 树上倍增


# 链接：https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/solutions/2305895/mo-ban-jiang-jie-shu-shang-bei-zeng-suan-v3rw/
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 的二进制从低到高第 i 位是 1
                node = self.pa[node][i]
                if node < 0:
                    break
        return node

    # 另一种写法，不断去掉 k 的最低位的 1
    def getKthAncestor2(self, node: int, k: int) -> int:
        while k and node != -1:  # 也可以写成 ~node
            lb = k & -k
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    parent: List[int] = deserialize("List[int]", constructor_params[1])
    obj = TreeAncestor(n, parent)

    for i in range(1, len(ops)):
        match ops[i]:
            case "getKthAncestor":
                method_params = split_array(params[i])
                node: int = deserialize("int", method_params[0])
                k: int = deserialize("int", method_params[1])
                ans = serialize(obj.getKthAncestor(node, k))
                output.append(ans)

    print("\noutput:", join_array(output))
