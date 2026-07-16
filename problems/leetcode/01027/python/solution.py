# Created by shiyang07ca at 2023/04/30 13:44
# https://leetcode.cn/problems/longest-arithmetic-subsequence/

"""
1027. 最长等差数列 (Medium)
给你一个整数数组 `nums`，返回 `nums` 中最长等差子序列的 **长
度**。

回想一下， `nums` 的子序列是一个列表 `nums[i₁], nums[i₂], ..
., nums[iₖ]` ，且 `0 <= i₁ < i₂ < ... < iₖ <= nums.length -
1`。并且如果 `seq[i+1] - seq[i]`( `0 <= i < seq.length - 1`)
的值都相同，那么序列 `seq` 是等差的。

**示例 1：**

```
输入：nums = [3,6,9,12]
输出：4
解释：
整个数组是公差为 3 的等差数列。

```

**示例 2：**

```
输入：nums = [9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。

```

**示例 3：**

```
输入：nums = [20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。

```

**提示：**

- `2 <= nums.length <= 1000`
- `0 <= nums[i] <= 500`

"""

from typing import *
from functools import *

from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp

"""
作者：灵茶山艾府
链接：https://leetcode.cn/problems/longest-arithmetic-subsequence/solutions/2239191/ji-yi-hua-sou-suo-di-tui-chang-shu-you-h-czvx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

定义 dfs(i)， 维护一个哈希表 maxLen, 表示所以以 a[i] 结尾的（至少有两个元素的）
LAS 的公差和对应长度。

从 i-1 倒序枚举 j，如果 d 不在 dfs(j) 返回的 maxLen 中，则 dfs(j)[d] = 1, 相当于
a[j] 是 LAS 的首项。

计算从 dfs(1) 到 dfs(n-1) 的所有哈希表中的 LAS 的长度的最大值

"""


class Solution:
    def longestArithSeqLength(self, a: List[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> dict[int, int]:
            # i=0 时不会进入循环，返回空哈希表
            max_len = {}
            for j in range(i - 1, -1, -1):
                d = a[i] - a[j]  # 公差
                if d not in max_len:
                    max_len[d] = dfs(j).get(d, 1) + 1
            return max_len

        return max(max(dfs(i).values()) for i in range(1, len(a)))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestArithSeqLength(nums)
    print("output:", serialize(ans))
