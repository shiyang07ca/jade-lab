# Created by shiyang07ca at 2024/01/20 20:59
# leetgo: dev
# https://leetcode.cn/problems/split-strings-by-separator/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            ws = w.split(separator)
            for c in ws:
                if c:
                    ans.append(c)
        return ans


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    separator: str = deserialize("str", read_line())
    ans = Solution().splitWordsBySeparator(words, separator)

    print("\noutput:", serialize(ans))
