# Created by shiyang07ca at 2023/06/28 12:42
# https://leetcode.cn/problems/minimum-incompatibility/

"""
1681. 最小不兼容性 (Hard)
给你一个整数数组 `nums`  和一个整数 `k` 。你需要将这个数组划
分到 `k` 个相同大小的子集中，使得同一个子集里面没有两个相同
的元素。

一个子集的 **不兼容性** 是该子集里面最大值和最小值的差。

请你返回将数组分成 `k` 个子集后，各子集 **不兼容性** 的 **和
** 的 **最小值** ，如果无法分成分成 `k` 个子集，返回 `-1` 。

子集的定义是数组中一些数字的集合，对数字顺序没有要求。

**示例 1：**

```
输入：nums = [1,2,1,4], k = 2
输出：4
解释：最优的分配是 [1,2] 和 [1,4] 。
不兼容性和为 (2-1) + (4-1) = 4 。
注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2
个相同的元素，所以不可行。
```

**示例 2：**

```
输入：nums = [6,3,8,1,3,1,2,2], k = 4
输出：6
解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。

```

**示例 3：**

```
输入：nums = [5,3,3,6,3,3], k = 3
输出：-1
解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相
同数字。

```

**提示：**

- `1 <= k <= nums.length <= 16`
- `nums.length` 能被 `k` 整除。
- `1 <= nums[i] <= nums.length`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp, bitmask


class Solution:
    def minimumIncompatibility(self, a: List[int], k: int) -> int:
        if any(c > k for c in Counter(a).values()):  # 鸽巢原理
            return -1

        n = len(a)
        size = n // k
        a.sort()  # 排序，便于判断重复

        # left 表示还剩下待选择的数的集合，pre 表示上一个选了哪个数
        @cache
        def dfs(left: int, pre: int) -> int:
            if left == 0:
                return 0
            if left.bit_count() % size == 0:  # 创建一个新的组
                lb = left & -left  # 选择 lowbit 作为第一个数
                return dfs(left ^ lb, lb.bit_length() - 1)
            res = inf
            last = a[pre]
            for i in range(pre + 1, n):  # 枚举这个组的下一个要选的数
                if left >> i & 1 and a[i] != last:  # 组内不能有重复数字，且 a 中重复数字只需枚举一次
                    last = a[i]
                    res = min(res, last - a[pre] + dfs(left ^ (1 << i), i))
            return res

        return dfs((1 << n) - 1, 0)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumIncompatibility(nums, k)
    print("output:", serialize(ans))
