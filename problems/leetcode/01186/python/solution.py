# Created by shiyang07ca at 2023/06/27 13:34
# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/

"""
1186. 删除一次得到子数组最大和 (Medium)
给你一个整数数组，返回它的某个 **非空** 子数组（连续元素）在
执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，
你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个
元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，
然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 **不能为空**。

**示例 1：**

```
输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1,
0, 3]，和最大。
```

**示例 2：**

```
输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。

```

**示例 3：**

```
输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中
删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个
-1。

```

**提示：**

- `1 <= arr.length <= 10⁵`
- `-10⁴ <= arr[i] <= 10⁴`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumSum1(self, arr: List[int]) -> int:
        n = len(arr)
        f1 = [0] * (n + 1)
        f2 = [0] * (n + 1)
        ans = -inf
        for i, x in enumerate(arr, 1):
            f1[i] = max(f1[i - 1] + x, x)
            ans = max(ans, f1[i])
        for i in range(n - 1, -1, -1):
            print(arr[i])
            f2[i] = max(f2[i + 1] + arr[i], arr[i])

        for i in range(1, n - 1):
            ans = max(ans, f1[i] + f2[i + 1])

        return ans

    # 链接：https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6/
    def maximumSum(self, arr: List[int]) -> int:
        # 定义 dfs(i,j) 表示子数组的右端点是 arr[i]，不能/必须删除数字的情况下，子数组元素和的最大值。
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return -inf  # 子数组至少要有一个数，不合法
            if j == 0:
                return max(dfs(i - 1, 0), 0) + arr[i]
            return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))

        return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(arr)
    print("output:", serialize(ans))
