from __future__ import annotations

# Created by shiyang07ca at 2024/01/10 07:42
# leetgo: dev
# https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" not in s and "CD" not in s:
                return len(s)
            s = s.replace("AB", "").replace("CD", "")


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minLength(s)

    print("\noutput:", serialize(ans))
