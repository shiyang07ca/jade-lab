# Created by shiyang07ca at 2023/05/27 20:43
# https://leetcode.cn/problems/statistics-from-a-large-sample/

"""
1093. 大样本统计 (Medium)
我们对 `0` 到 `255` 之间的整数进行采样，并将结果存储在数组 `count` 中： `count[k]` 就是整数 `k` 在样
本中出现的次数。

计算以下统计数据:

- `minimum` ：样本中的最小元素。
- `maximum` ：样品中的最大元素。
- `mean` ：样本的平均值，计算为所有元素的总和除以元素总数。
- `median` ：

  - 如果样本的元素个数是奇数，那么一旦样本排序后，中位数 `median` 就是中间的元素。
  - 如果样本中有偶数个元素，那么中位数 `median` 就是样本排序后中间两个元素的平均值。
- `mode` ：样本中出现次数最多的数字。保众数是 **唯一** 的。

以浮点数数组的形式返回样本的统计信息 `[minimum, maximum, mean, median, mode]` 。与真实答案误差在 `10
-⁵` 内的答案都可以通过。

**示例 1：**

```
输入：count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：[1.00000,3.00000,2.37500,2.50000,3.00000]
解释：用count表示的样本为[1,2,2,2,3,3,3,3]。
最小值和最大值分别为1和3。
均值是(1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375。
因为样本的大小是偶数，所以中位数是中间两个元素2和3的平均值，也就是2.5。
众数为3，因为它在样本中出现的次数最多。
```

**示例 2：**

```
输入：count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：[1.00000,4.00000,2.18182,2.00000,1.00000]
解释：用count表示的样本为[1,1,1,1,2,2,3,3,3,4,4]。
最小值为1，最大值为4。
平均数是(1+1+1+1+2+2+2+3+3+4+4)/ 11 = 24 / 11 = 2.18181818…(为了显示，输出显示了整数2.18182)。
因为样本的大小是奇数，所以中值是中间元素2。
众数为1，因为它在样本中出现的次数最多。

```

**提示：**

- `count.length == 256`
- `0 <= count[i] <= 10⁹`
- `1 <= sum(count) <= 10⁹`
- `count` 的众数是 **唯一** 的

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sampleStats1(self, count: List[int]) -> List[float]:
        mi = ma = mean = median = mode = -1
        tot = s = q = 0
        for n, c in enumerate(count):
            if mi == -1 and c > 0:
                mi = n
            if c > 0:
                ma = n
            tot += c * n
            s += c
            if c > q:
                q = c
                mode = n
        mean = tot / s

        t = 0
        if s % 2 == 1:
            for n, c in enumerate(count):
                t += c
                if t >= s // 2 + 1:
                    median = n
                    break
        if s % 2 == 0:
            ns = []
            for n, c in enumerate(count):
                t += c
                if not ns and t >= s // 2:
                    ns.append(n)
                if t >= s // 2 + 1:
                    ns.append(n)
                if len(ns) == 2:
                    median = sum(ns) / 2
                    break
        return float(mi), float(ma), mean, median, float(mode)

    # 链接：https://leetcode.cn/problems/statistics-from-a-large-sample/solutions/2285421/python3javacgotypescript-yi-ti-yi-jie-mo-ov62/
    def sampleStats(self, count: List[int]) -> List[float]:
        def find(i: int) -> int:
            t = 0
            for k, x in enumerate(count):
                t += x
                if t >= i:
                    return k

        mi, mx = inf, -1
        s = cnt = 0
        mode = 0
        for k, x in enumerate(count):
            if x:
                mi = min(mi, k)
                mx = max(mx, k)
                s += k * x
                cnt += x
                if x > count[mode]:
                    mode = k

        median = (
            find(cnt // 2 + 1) if cnt & 1 else (find(cnt // 2) + find(cnt // 2 + 1)) / 2
        )
        return [mi, mx, s / cnt, median, mode]


# @lc code=end

if __name__ == "__main__":
    count: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sampleStats(count)

    print("\noutput:", serialize(ans))
