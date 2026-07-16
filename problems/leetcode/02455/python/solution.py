# Created by shiyang07ca at 2023/05/29 08:15
# https://leetcode.cn/problems/average-value-of-even-numbers-that-are-divisible-by-three/

"""
2455. 可被三整除的偶数的平均值 (Easy)
给你一个由正整数组成的整数数组 `nums` ，返回其中可被 `3` 整除的所有偶数的平均值。

注意： `n` 个元素的平均值等于 `n` 个元素 **求和** 再除以 `n` ，结果 **向下取整** 到最接近的整数。

**示例 1：**

```
输入：nums = [1,3,6,10,12,15]
输出：9
解释：6 和 12 是可以被 3 整除的偶数。(6 + 12) / 2 = 9 。

```

**示例 2：**

```
输入：nums = [1,2,4,7,10]
输出：0
解释：不存在满足题目要求的整数，所以返回 0 。

```

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = [n for n in nums if n % 3 == 0 and n % 2 == 0]
        return sum(ans) // len(ans) if ans else 0


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().averageValue(nums)

    print("\noutput:", serialize(ans))
