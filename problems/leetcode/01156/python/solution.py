# Created by shiyang07ca at 2023/06/03 00:56
# https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/

"""
1156. 单字符重复子串的最大长度 (Medium)
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 `text`，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回
其中最长的子串的长度。

**示例 1：**

```
输入：text = "ababa"
输出：3

```

**示例 2：**

```
输入：text = "aaabaaa"
输出：6

```

**示例 3：**

```
输入：text = "aaabbaaa"
输出：4

```

**示例 4：**

```
输入：text = "aaaaa"
输出：5

```

**示例 5：**

```
输入：text = "abcdef"
输出：1

```

**提示：**

- `1 <= text.length <= 20000`
- `text` 仅由小写英文字母组成。

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/solutions/2294588/python3javacgotypescript-yi-ti-yi-jie-sh-uq9g/
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        n = len(text)
        ans = i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            left = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            right = k - j - 1
            ans = max(ans, min(left + right + 1, cnt[text[i]]))
            i = j
        return ans


# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().maxRepOpt1(text)

    print("\noutput:", serialize(ans))
