# Created by shiyang07ca at 2023/05/12 12:34
# https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/

"""
1330. 翻转子数组得到最大的数组值 (Hard)
给你一个整数数组 `nums` 。「数组值」定义为所有满足 `0 <= i <
nums.length-1` 的 `|nums[i]-nums[i+1]|` 的和。

你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执
行这个操作 **一次** 。

请你找到可行的最大 **数组值**。

**示例 1：**

```
输入：nums = [2,3,1,5,4]
输出：10
解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值
为 10 。

```

**示例 2：**

```
输入：nums = [2,4,9,24,2,1,10]
输出：68

```

**提示：**

- `1 <= nums.length <= 3*10^4`
- `-10^5 <= nums[i] <= 10^5`

"""
from itertools import *
from math import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: math


class Solution:
    # https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/solutions/2266682/python3javacgotypescript-yi-ti-yi-jie-fe-3ygf/
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        ans = s = sum(abs(x - y) for x, y in pairwise(nums))
        for x, y in pairwise(nums):
            ans = max(ans, s + abs(nums[0] - y) - abs(x - y))
            ans = max(ans, s + abs(nums[-1] - x) - abs(x - y))
        for k1, k2 in pairwise((1, -1, -1, 1, 1)):
            mx, mi = -inf, inf
            for x, y in pairwise(nums):
                a = k1 * x + k2 * y
                b = abs(x - y)
                mx = max(mx, a - b)
                mi = min(mi, a + b)
            ans = max(ans, s + max(mx - mi, 0))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxValueAfterReverse(nums)
    print("output:", serialize(ans))
