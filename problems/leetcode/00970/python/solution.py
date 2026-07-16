# Created by shiyang07ca at 2023/05/02 14:07
# https://leetcode.cn/problems/powerful-integers/

"""
970. 强整数 (Medium)
给定三个整数 `x` 、 `y` 和 `bound`，返回 值小于或等于 `bound
` 的所有 **强整数** 组成的列表 。

如果某一整数可以表示为 `xⁱ + yj` ，其中整数 `i >= 0` 且 `j >
= 0`，那么我们认为该整数是一个 **强整数** 。

你可以按 **任何顺序** 返回答案。在你的回答中，每个值 **最多*
* 出现一次。

**示例 1：**

```
输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释：
2 = 2⁰ + 3⁰
3 = 2¹ + 3⁰
4 = 2⁰ + 3¹
5 = 2¹ + 3¹
7 = 2² + 3¹
9 = 2³ + 3⁰
10 = 2⁰ + 3²
```

**示例 2：**

```
输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]

```

**提示：**

- `1 <= x, y <= 100`
- `0 <= bound <= 10⁶`

"""

from math import *
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        for i in range(21):
            for j in range(21):
                t = x**i + y**j
                if t <= bound:
                    ans.add(t)
                else:
                    break

        return list(ans)


# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    bound: int = deserialize("int", read_line())
    ans = Solution().powerfulIntegers(x, y, bound)
    print("output:", serialize(ans))
