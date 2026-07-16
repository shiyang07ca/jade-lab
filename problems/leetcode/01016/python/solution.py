# Created by shiyang07ca at 2023/05/11 00:03
# https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/

"""
1016. 子串能表示从 1 到 N 数字的二进制串 (Medium)
给定一个二进制字符串 `s` 和一个正整数 `n`，如果对于 `[1, n]`
范围内的每个整数，其二进制表示都是 `s` 的 **子字符串** ，就
返回 `true`，否则返回 `false`。

**子字符串** 是字符串中连续的字符序列。

**示例 1：**

```
输入：s = "0110", n = 3
输出：true

```

**示例 2：**

```
输入：s = "0110", n = 4
输出：false

```

**提示：**

- `1 <= s.length <= 1000`
- `s[i]` 不是 `'0'` 就是 `'1'`
- `1 <= n <= 10⁹`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def queryString1(self, s: str, n: int) -> bool:
        return all(bin(i)[2:] in s for i in range(1, n + 1))

    # https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/solutions/2265097/san-chong-suan-fa-cong-bao-li-dao-you-hu-nmtq/
    def queryString(self, s: str, n: int) -> bool:
        seen = set()
        s = list(map(int, s))
        for i, x in enumerate(s):
            if x == 0:
                continue  # 从第一个 1 开始枚举
            j = i + 1  # 计算子串 [i:j] 对应的二进制数
            while x <= n:
                seen.add(x)
                if j >= len(s):
                    break
                x = (x << 1) | s[j]  # 子串 s[i:j] 对应的二进制数
                j += 1
        return len(seen) == n


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().queryString(s, n)
    print("output:", serialize(ans))
