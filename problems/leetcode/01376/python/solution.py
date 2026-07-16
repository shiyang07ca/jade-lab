# Created by shiyang07ca at 2023/05/01 11:31
# https://leetcode.cn/problems/time-needed-to-inform-all-employees/

"""
1376. 通知所有员工所需的时间 (Medium)
公司里有 `n` 名员工，每个员工的 ID 都是独一无二的，编号从 `0
` 到 `n - 1`。公司的总负责人通过 `headID` 进行标识。

在 `manager` 数组中，每个员工都有一个直属负责人，其中 `manag
er[i]` 是第 `i` 名员工的直属负责人。对于总负责人， `manager[
headID] = -1`。题目保证从属关系可以用树结构显示。

公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通
知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员
工都得知这条紧急消息。

第 `i` 名员工需要 `informTime[i]` 分钟来通知它的所有直属下属
（也就是说在 `informTime[i]` 分钟后，他的所有直属下属都可以
开始传播这一消息）。

返回通知所有员工这一紧急消息所需要的 **分钟数** 。

**示例 1：**

```
输入：n = 1, headID = 0, manager = [-1], informTime = [0]
输出：0
解释：公司总负责人是该公司的唯一一名员工。

```

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/
2020/03/08/graph.png)

```
输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTim
e = [0,0,1,0,0,0]
输出：1
解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属
负责人，他需要 1 分钟来通知所有员工。
上图显示了公司员工的树结构。

```

**提示：**

- `1 <= n <= 10^5`
- `0 <= headID < n`
- `manager.length == n`
- `0 <= manager[i] < n`
- `manager[headID] == -1`
- `informTime.length == n`
- `0 <= informTime[i] <= 1000`
- 如果员工 `i` 没有下属， `informTime[i] == 0` 。
- 题目 **保证** 所有员工都可以收到通知。

"""

from typing import *
from functools import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dfs, bfs

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/time-needed-to-inform-all-employees/solutions/2251986/shen-ru-li-jie-di-gui-zi-ding-xiang-xia-ps0mm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:

    """
    方法一：自顶向下
    """

    # 返回值写法
    def numOfMinutes1(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                g[m].append(i)  # 建树

        def dfs(x: int) -> int:
            max_path_sum = 0
            for y in g[x]:  # 遍历 x 的儿子 y（如果没有儿子就不会进入循环）
                max_path_sum = max(max_path_sum, dfs(y))
            # 这和 104 题代码中的 max(l_depth, r_depth) + 1 是一个意思
            return max_path_sum + informTime[x]

        return dfs(headID)  # 从根节点 headID 开始递归

    # 传参写法
    def numOfMinutes2(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                g[m].append(i)  # 建树
        ans = 0

        def dfs(x: int, path_sum: int) -> None:
            path_sum += informTime[x]  # 累加递归路径上的 informTime[x]
            nonlocal ans
            ans = max(ans, path_sum)  # 更新答案的最大值
            for y in g[x]:  # 遍历 x 的儿子 y（如果没有儿子就不会进入循环）
                dfs(y, path_sum)  # 继续递归

        dfs(headID, 0)  # 从根节点 headID 开始递归
        return ans

    """
    方法二：自底向上

    由于 manager 数组中保存了每个节点的父节点，无需建树，直接顺着父节点，一路向
    上，同时累加路径上的 informTime[x]。
    """

    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(x: int) -> int:
            if manager[x] < 0:
                return informTime[x]
            return dfs(manager[x]) + informTime[x]

        return max(dfs(i) for i in range(n))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    headID: int = deserialize("int", read_line())
    manager: List[int] = deserialize("List[int]", read_line())
    informTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numOfMinutes(n, headID, manager, informTime)
    print("output:", serialize(ans))
