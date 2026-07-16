# Created by shiyang07ca at 2023/05/16 08:53
# https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/

"""
1335. 工作计划的最低难度 (Hard)
你需要制定一份 `d` 天的工作计划表。工作之间存在依赖，要想执行第 `i` 项工作，你必须完成全部 `j` 项工
作（ `0 <= j < i`）。

你每天 **至少** 需要完成一项任务。工作计划的总难度是这 `d` 天每一天的难度之和，而一天的工作难度是当
天应该完成工作的最大难度。

给你一个整数数组 `jobDifficulty` 和一个整数 `d`，分别代表工作难度和需要计划的天数。第 `i` 项工作的难
度是 `jobDifficulty[i]`。

返回整个工作计划的 **最小难度** 。如果无法制定工作计划，则返回 **-1**。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/26/untitled.png)

```
输入：jobDifficulty = [6,5,4,3,2,1], d = 2
输出：7
解释：第一天，您可以完成前 5 项工作，总难度 = 6.
第二天，您可以完成最后一项工作，总难度 = 1.
计划表的难度 = 6 + 1 = 7

```

**示例 2：**

```
输入：jobDifficulty = [9,9,9], d = 4
输出：-1
解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。

```

**示例 3：**

```
输入：jobDifficulty = [1,1,1], d = 3
输出：3
解释：工作计划为每天一项工作，总难度为 3 。

```

**示例 4：**

```
输入：jobDifficulty = [7,1,7,1,7,1], d = 3
输出：15

```

**示例 5：**

```
输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
输出：843

```

**提示：**

- `1 <= jobDifficulty.length <= 300`
- `0 <= jobDifficulty[i] <= 1000`
- `1 <= d <= 10`

"""
from itertools import *
from functools import *
from math import *

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: dp


class Solution:
    def minDifficulty1(self, jd: List[int], d: int) -> int:
        if len(jd) < d:
            return -1

        @cache
        def dfs(i, j, k):  # i 当前位置，j 上一个位置, k 还剩几天
            if len(jd) - i < k:
                return inf
            if i >= len(jd) or k == 1:
                return max(jd[j:])
            return min(dfs(i + 1, j, k), dfs(i + 1, i + 1, k - 1) + max(jd[j : i + 1]))

        return dfs(0, 0, d)

    # 链接：https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/solutions/2271631/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-68nx/
    def minDifficulty2(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        # dfs(i,j) 表示用 i+1 天时间完成 a[0] 到 a[j] 这些工作的答案
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == 0:  # 只有一天，必须完成所有工作
                return max(a[: j + 1])
            res, mx = inf, 0
            for k in range(j, i - 1, -1):
                mx = max(mx, a[k])  # 从 a[k] 到 a[j] 的最大值
                res = min(res, dfs(i - 1, k - 1) + mx)
            return res

        return dfs(d - 1, n - 1)

    # TODO：
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        f = [[inf] * n for _ in range(d)]
        f[0] = list(accumulate(a, max))
        for i in range(1, d):
            for j in range(i, n):
                mx = 0
                for k in range(j, i - 1, -1):
                    mx = max(mx, a[k])  # 从 a[k] 到 a[j] 的最大值
                    f[i][j] = min(f[i][j], f[i - 1][k - 1] + mx)
        return f[-1][-1]


# @lc code=end

if __name__ == "__main__":
    jobDifficulty: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().minDifficulty(jobDifficulty, d)

    print("\noutput:", serialize(ans))
