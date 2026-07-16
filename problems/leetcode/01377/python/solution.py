# Created by shiyang07ca at 2023/05/24 10:02
# https://leetcode.cn/problems/frog-position-after-t-seconds/

"""
1377. T 秒后青蛙的位置 (Hard)
给你一棵由 `n` 个顶点组成的无向树，顶点编号从 `1` 到 `n`。青蛙从 **顶点 1** 开始起跳。规则如下：

- 在一秒内，青蛙从它所在的当前顶点跳到另一个 **未访问** 过的顶点（如果它们直接相连）。
- 青蛙无法跳回已经访问过的顶点。
- 如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
- 如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。

无向树的边用数组 `edges` 描述，其中 `edges[i] = [aᵢ, bᵢ]` 意味着存在一条直接连通 `aᵢ` 和 `bᵢ` 两个顶
点的边。

返回青蛙在 `t` 秒后位于目标顶点 `target`上的概率。与实际答案相差不超过 `10-⁵` 的结果将被视为正确答案
。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/12/21/frog1.jpg)

```
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
输出：0.16666666666666666
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有
1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/12/21/frog2.jpg)

```
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
输出：0.3333333333333333
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳
到顶点 7 。

```

**提示：**

- `1 <= n <= 100`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= aᵢ, bᵢ <= n`
- `1 <= t <= 50`
- `1 <= target <= n`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def frogPosition1(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = set()

        def dfs(i, t, cur):
            if i == target and (t == 0 or len(g[target]) == 1):
                return cur
            elif (t == 0 and i != target) or (t > 0 and i == target and len(g[i]) > 1):
                return 0

            vis.add(i)
            for j in g[i]:
                if j not in vis:
                    vis.add(j)
                    ps = len(g[i]) if i == 1 else len(g[i]) - 1
                    ans = dfs(j, t - 1, cur * ps)
                    if ans > 0:
                        return ans
            return 0

        if target == 1:
            if t >= 1 and len(g[1]) >= 1:
                return 0.0
            else:
                return 1.0

        cur = dfs(1, t, 1)
        if cur > 0:
            return 1 / cur
        else:
            return 0.0

        # 链接：https://leetcode.cn/problems/frog-position-after-t-seconds/solutions/2281408/dfs-ji-yi-ci-you-qu-de-hack-by-endlessch-jtsr/

    def frogPosition2(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        g = [[] for _ in range(n + 1)]
        g[1] = [0]  # 减少额外判断的小技巧
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建树
        ans = 0

        def dfs(x: int, fa: int, left_t: int, prod: int) -> True:
            # t 秒后必须在 target（恰好到达，或者 target 是叶子停在原地）
            if x == target and (left_t == 0 or len(g[x]) == 1):
                nonlocal ans
                ans = 1 / prod
                return True
            if x == target or left_t == 0:
                return False
            for y in g[x]:  # 遍历 x 的儿子 y
                if y != fa and dfs(y, x, left_t - 1, prod * (len(g[x]) - 1)):
                    return True  # 找到 target 就不再递归了
            return False  # 未找到 target

        dfs(1, 0, t, 1)
        return ans

    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        g = [[] for _ in range(n + 1)]
        g[1] = [0]  # 减少额外判断的小技巧
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建树

        def dfs(x: int, fa: int, left_t: int) -> int:
            # t 秒后必须在 target（恰好到达，或者 target 是叶子停在原地）
            if left_t == 0:
                return x == target
            if x == target:
                return len(g[x]) == 1
            for y in g[x]:  # 遍历 x 的儿子 y
                if y != fa:  # y 不能是父节点
                    prod = dfs(y, x, left_t - 1)  # 寻找 target
                    if prod:
                        return prod * (len(g[x]) - 1)  # 乘上儿子个数，并直接返回
            return 0  # 未找到 target

        prod = dfs(1, 0, t)
        return 1 / prod if prod else 0


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    t: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().frogPosition(n, edges, t, target)

    print("\noutput:", serialize(ans))
