from __future__ import annotations

# Created by shiyang07ca at 2023/12/20 12:47
# leetgo: dev
# https://leetcode.cn/problems/check-if-a-string-is-an-acronym-of-words/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        return "".join(w[0] for w in words) == s


# @lc code=end

if __name__ == "__main__":
    words: list[str] = deserialize("List[str]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().isAcronym(words, s)

    print("\noutput:", serialize(ans))
