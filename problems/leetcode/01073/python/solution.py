# Created by shiyang07ca at 2023/05/18 08:24
# https://leetcode.cn/problems/adding-two-negabinary-numbers/

"""
1073. 负二进制数相加 (Medium)
给出基数为 **-2** 的两个数 `arr1` 和 `arr2`，返回两数相加的结果。

数字以 数组形式给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如， `arr = [1,1,
0,1]` 表示数字 `(-2)^3 + (-2)^2 + (-2)^0 = -3`。数组形式 中的数字 `arr` 也同样不含前导零：即 `arr ==
[0]` 或 `arr[0] == 1`。

返回相同表示形式的 `arr1` 和 `arr2` 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数
组。

**示例 1：**

```
输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
输出：[1,0,0,0,0]
解释：arr1 表示 11，arr2 表示 5，输出表示 16 。

```

**示例 2：**

```
输入：arr1 = [0], arr2 = [0]
输出：[0]

```

**示例 3：**

```
输入：arr1 = [0], arr2 = [1]
输出：[1]

```

**提示：**

- `1 <= arr1.length, arr2.length <= 1000`
- `arr1[i]` 和 `arr2[i]` 都是 `0` 或 `1`
- `arr1` 和 `arr2` 都没有前导0

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def addNegabinary1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def baseNeg2(n: int) -> List[int]:
            if n == 0:
                return [0]
            if n == 1:
                return [1]
            if n & 1:
                return baseNeg2((n - 1) // -2) + [1]
            else:
                return baseNeg2(n // -2) + [0]

        def to10(arr: List[int]) -> List[int]:
            return sum((-2) ** (len(arr) - i - 1) for i, n in enumerate(arr) if n)

        return baseNeg2(int(to10(arr1) + to10(arr2)))

    # 链接：https://leetcode.cn/problems/adding-two-negabinary-numbers/solutions/2273578/fu-er-jin-zhi-shu-xiang-jia-by-leetcode-nwktq/
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        ans = list()

        while i >= 0 or j >= 0 or carry:
            x = carry
            if i >= 0:
                x += arr1[i]
            if j >= 0:
                x += arr2[j]

            if x >= 2:
                ans.append(x - 2)
                carry = -1
            elif x >= 0:
                ans.append(x)
                carry = 0
            else:
                ans.append(1)
                carry = 1
            i -= 1
            j -= 1

        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ans[::-1]


# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().addNegabinary(arr1, arr2)

    print("\noutput:", serialize(ans))
