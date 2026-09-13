from __future__ import annotations

# Created by shiyang07ca at 2024/03/11 00:02
# leetgo: dev
# https://leetcode.cn/problems/capitalize-the-title/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ts = title.split(" ")
        ans = []
        for t in ts:
            if len(t) in (1, 2):
                ans.append(t.lower())
            else:
                ans.append(t[0].upper() + t[1:].lower())
        return " ".join(ans)


# @lc code=end

if __name__ == "__main__":
    title: str = deserialize("str", read_line())
    ans = Solution().capitalizeTitle(title)

    print("\noutput:", serialize(ans))
