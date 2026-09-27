# Created by shiyang07ca at 2026/09/27 13:32
# leetgo: 1.4.17
# https://leetcode.cn/problems/decode-string/

from typing import *

from leetgo_py import *

# @lc code=begin


# TODO
class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        cur = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stk.append((cur, num))
                cur = ""
                num = 0
            elif ch == "]":
                pre, repeat = stk.pop()
                cur = pre + cur * repeat
            else:
                cur += ch

        return cur


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().decodeString(s)
    print("\noutput:", serialize(ans, "string"))
