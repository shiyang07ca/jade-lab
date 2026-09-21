from __future__ import annotations

from collections import defaultdict

# Created by shiyang07ca at 2023/11/26 21:02
# leetgo: dev
# https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/solutions/2542059/python3javacgotypescriptrust-yi-ti-yi-ji-azbp/
    def uniqueLetterString(self, s: str) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        ans = 0
        for v in d.values():
            v = [-1] + v + [len(s)]
            for i in range(1, len(v) - 1):
                ans += (v[i] - v[i - 1]) * (v[i + 1] - v[i])
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().uniqueLetterString(s)

    print("\noutput:", serialize(ans))
