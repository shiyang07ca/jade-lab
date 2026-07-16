# Created by shiyang07ca at 2023/06/19 08:37
# https://leetcode.cn/problems/greatest-sum-divisible-by-three/

"""
1262. 可被三整除的最大和 (Medium)
给你一个整数数组 `nums`，请你找出并返回能被三整除的元素最大和。

**示例 1：**

```
输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
```

**示例 2：**

```
输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。

```

**示例 3：**

```
输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。

```

**提示：**

- `1 <= nums.length <= 4 * 10^4`
- `1 <= nums[i] <= 10^4`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp, greedy

# https://leetcode.cn/problems/greatest-sum-divisible-by-three/solutions/45481/fei-chang-po-su-de-xiang-fa-wu-dp-by-sherryokok/


class Solution:
    def maxSumDivThree1(self, nums: List[int]) -> int:
        ans = sum(nums)
        a1, a2 = [], []
        for n in nums:
            if n % 3 == 1:
                a1.append(n)
            elif n % 3 == 2:
                a2.append(n)
        a1.sort()
        a2.sort()

        if ans % 3 == 1:
            t0 = t1 = inf
            if len(a1) >= 1:
                t0 = a1[0]
            if len(a2) >= 2:
                t1 = a2[0] + a2[1]
            ans -= min(t0, t1)
        elif ans % 3 == 2:
            t0 = t1 = inf
            if len(a1) >= 2:
                t0 = a1[0] + a1[1]
            if len(a2) >= 1:
                t1 = a2[0]
            ans -= min(t0, t1)

        return ans

    # 链接：https://leetcode.cn/problems/greatest-sum-divisible-by-three/solutions/2313700/liang-chong-suan-fa-tan-xin-dong-tai-gui-tsll/
    def maxSumDivThree2(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s
        a1 = sorted(x for x in nums if x % 3 == 1)
        a2 = sorted(x for x in nums if x % 3 == 2)
        if s % 3 == 2:
            a1, a2 = a2, a1
        ans = s - a1[0] if a1 else 0
        if len(a2) > 1:
            ans = max(ans, s - a2[0] - a2[1])
        return ans

    # 链接：https://leetcode.cn/problems/greatest-sum-divisible-by-three/solutions/2313700/liang-chong-suan-fa-tan-xin-dong-tai-gui-tsll/
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        定义 dfs(i, j) 表示 nums[0] 到 nums[i] 中选数，已选数字之和 mod 3 = j 的最大值
        则有：dfs(i, j) = max(dfs(i - 1, j),  不选 x
                              dfs(i - 1, (j + x) mod 3) + x,  选 x
        递归边界：dfs(−1,0)=0, dfs(−1,1)=−∞, dfs(−1,2)=−∞
        """

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return -inf if j else 0
            return max(dfs(i - 1, j), dfs(i - 1, (j + nums[i]) % 3) + nums[i])

        return dfs(len(nums) - 1, 0)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSumDivThree(nums)

    print("\noutput:", serialize(ans))
