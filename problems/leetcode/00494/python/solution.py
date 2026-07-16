# Created by shiyang07ca at 2023/05/03 21:39
# https://leetcode.cn/problems/target-sum/

"""
494. 目标和 (Medium)
给你一个整数数组 `nums` 和一个整数 `target` 。

向数组中的每个整数前添加 `'+'` 或 `'-'` ，然后串联起所有整数
，可以构造一个 **表达式** ：

- 例如， `nums = [2, 1]` ，可以在 `2` 之前添加 `'+'` ，在 `1
` 之前添加 `'-'` ，然后串联起来得到表达式 `"+2-1"` 。

返回可以通过上述方法构造的、运算结果等于 `target` 的不同 **
表达式** 的数目。

**示例 1：**

```
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

```

**示例 2：**

```
输入：nums = [1], target = 1
输出：1

```

**提示：**

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

"""
from functools import *
from typing import *
from leetgo_py import *

# @lc code=begin

# template
# tag: dp, knapsack


class Solution:
    # 记忆化搜索
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        # 找到正号总和 p，nums 总和为 s, 负号总和为 s-p
        # p - (s-p) = t
        # => 2p = s + t
        # => p = (s + t) / 2
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

        return dfs(n - 1, target)

    # 递推
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]
        return f[n][target]

    # 滚动数组更新
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        f = [0] * (target + 1)
        f[0] = 1
        for x in nums:
            for c in range(target, x - 1, -1):
                f[c] = f[c] + f[c - x]
        return f[target]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findTargetSumWays(nums, target)
    print("output:", serialize(ans))
