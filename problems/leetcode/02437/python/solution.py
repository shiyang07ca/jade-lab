# Created by shiyang07ca at 2023/05/09 13:03
# https://leetcode.cn/problems/number-of-valid-clock-times/

"""
2437. 有效时间的数目 (Easy)
给你一个长度为 `5` 的字符串 `time` ，表示一个电子时钟当前的
时间，格式为 `"hh:mm"` 。 **最早** 可能的时间是 `"00:00"` ，
**最晚** 可能的时间是 `"23:59"` 。

在字符串 `time` 中，被字符 `?` 替换掉的数位是 **未知的** ，
被替换的数字可能是 `0` 到 `9` 中的任何一个。

请你返回一个整数 `answer` ，将每一个 `?` 都用 `0` 到 `9` 中
一个数字替换后，可以得到的有效时间的数目。

**示例 1：**

```
输入：time = "?5:00"
输出：2
解释：我们可以将 ? 替换成 0 或 1 ，得到 "05:00" 或者 "15:00"
。注意我们不能替换成 2 ，因为时间 "25:00" 是无效时间。所以我
们有两个选择。

```

**示例 2：**

```
输入：time = "0?:0?"
输出：100
解释：两个 ? 都可以被 0 到 9 之间的任意数字替换，所以我们总
共有 100 种选择。

```

**示例 3：**

```
输入：time = "??:??"
输出：1440
解释：小时总共有 24 种选择，分钟总共有 60 种选择。所以总共有
24 * 60 = 1440 种选择。

```

**提示：**

- `time` 是一个长度为 `5` 的有效字符串，格式为 `"hh:mm"` 。
- `"00" <= hh <= "23"`
- `"00" <= mm <= "59"`
- 字符串中有的数位是 `'?'` ，需要用 `0` 到 `9` 之间的数字替
换。

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countTime1(self, time: str) -> int:
        def cnt(s, upbound):
            if "?" not in s:
                return 1
            c = 0
            if s[0] == "?" and s[1] != "?":
                for i in range(10):
                    if i * 10 + int(s[1]) > upbound:
                        return c
                    else:
                        c += 1
            elif s[0] != "?" and s[1] == "?":
                for i in range(10):
                    if int(s[0]) * 10 + i > upbound:
                        return c
                    elif i == 9:
                        return 10
                    else:
                        c += 1
            else:
                return upbound + 1

        a, b = time.split(":")
        a, b = cnt(a, 23), cnt(b, 59)
        return a * b

    # 作者：ylb
    # 链接：https://leetcode.cn/problems/number-of-valid-clock-times/solutions/2262415/python3javacgotypescript-yi-ti-shuang-ji-shsr/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def countTime(self, time: str) -> int:
        def check(s: str, t: str) -> bool:
            return all(a == b or b == "?" for a, b in zip(s, t))

        return sum(
            check(f"{h:02d}:{m:02d}", time) for h in range(24) for m in range(60)
        )


# @lc code=end

if __name__ == "__main__":
    time: str = deserialize("str", read_line())
    ans = Solution().countTime(time)
    print("output:", serialize(ans))
