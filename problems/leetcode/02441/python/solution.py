# Created by shiyang07ca at 2023/05/13 00:18
# https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/

"""
2441. 与对应负数同时存在的最大正整数 (Easy)
给你一个 **不包含** 任何零的整数数组 `nums` ，找出自身与对应
的负数都在数组中存在的最大正整数 `k` 。

返回正整数 `k` ，如果不存在这样的整数，返回 `-1` 。

**示例 1：**

```
输入：nums = [-1,2,-3,3]
输出：3
解释：3 是数组中唯一一个满足题目要求的 k 。

```

**示例 2：**

```
输入：nums = [-1,10,6,7,-7,1]
输出：7
解释：数组中存在 1 和 7 对应的负数，7 的值更大。

```

**示例 3：**

```
输入：nums = [-10,8,6,7,-2,-3]
输出：-1
解释：不存在满足题目要求的 k ，返回 -1 。

```

**提示：**

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `nums[i] != 0`

"""
from collections import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        cnt = Counter(nums)
        for n in sorted(cnt.keys(), reverse=True):
            if n > 0:
                if cnt[-n] >= 1:
                    ans = max(ans, n)
            else:
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaxK(nums)
    print("output:", serialize(ans))
