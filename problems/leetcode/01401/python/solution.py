# Created by shiyang07ca at 2023/06/25 12:51
# https://leetcode.cn/problems/circle-and-rectangle-overlapping/

"""
1401. 圆和矩形是否有重叠 (Medium)
给你一个以 `(radius, xCenter, yCenter)` 表示的圆和一个与坐标
轴平行的矩形 `(x1, y1, x2, y2)` ，其中 `(x1, y1)` 是矩形左下
角的坐标，而 `(x2, y2)` 是右上角的坐标。

如果圆和矩形有重叠的部分，请你返回 `true` ，否则返回 `false`
。

换句话说，请你检测是否 **存在** 点 `(xᵢ, yᵢ)` ，它既在圆上也
在矩形上（两者都包括点落在边界上的情况）。

**示例 1 ：**

![](https://assets.leetcode.com/uploads/2020/02/20/sample_4_
1728.png)

```
输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1,
x2 = 3, y2 = 1
输出：true
解释：圆和矩形存在公共点 (1,0) 。

```

**示例 2 ：**

```
输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3,
x2 = 2, y2 = -1
输出：false

```

**示例 3 ：**

![](https://assets.leetcode.com/uploads/2020/02/20/sample_2_
1728.png)

```
输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0,
x2 = 0, y2 = 1
输出：true

```

**提示：**

- `1 <= radius <= 2000`
- `-10⁴ <= xCenter, yCenter <= 10⁴`
- `-10⁴ <= x1 < x2 <= 10⁴`
- `-10⁴ <= y1 < y2 <= 10⁴`

"""
from math import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkOverlap1(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        def check(x1, y1, x2, y2):
            # return abs(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - radius) <= 0.0000000001
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= radius

        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True
        elif xCenter <= x1 and yCenter >= y2:
            return check(xCenter, yCenter, x1, y2)
        elif xCenter <= x1 and yCenter <= y1:
            return check(xCenter, yCenter, x1, y1)
        elif xCenter >= x2 and yCenter >= y2:
            return check(xCenter, yCenter, x2, y2)
        elif xCenter >= x2 and yCenter <= y1:
            return check(xCenter, yCenter, x2, y1)
        elif xCenter <= x1 and y1 <= yCenter <= y2:
            return abs(xCenter - x1) <= radius
        elif xCenter >= x2 and y1 <= yCenter <= y2:
            return abs(xCenter - x2) <= radius
        elif x1 <= xCenter <= x2 and yCenter <= y1:
            return abs(yCenter - y1) <= radius
        elif x1 <= xCenter <= x2 and yCenter >= y2:
            return abs(yCenter - y2) <= radius

        return False

    # 链接：https://leetcode.cn/problems/circle-and-rectangle-overlapping/solutions/2319357/python3javacgotypescript-yi-ti-yi-jie-sh-vpsu/
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        def f(i: int, j: int, k: int) -> int:
            if i <= k <= j:
                return 0
            return i - k if k < i else k - j

        a = f(x1, x2, xCenter)
        b = f(y1, y2, yCenter)
        return a * a + b * b <= radius * radius


# @lc code=end

if __name__ == "__main__":
    radius: int = deserialize("int", read_line())
    xCenter: int = deserialize("int", read_line())
    yCenter: int = deserialize("int", read_line())
    x1: int = deserialize("int", read_line())
    y1: int = deserialize("int", read_line())
    x2: int = deserialize("int", read_line())
    y2: int = deserialize("int", read_line())
    ans = Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    print("output:", serialize(ans))
