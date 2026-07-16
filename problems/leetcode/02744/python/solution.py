# Created by shiyang07ca at 2024/01/17 13:24
# leetgo: dev
# https://leetcode.cn/problems/find-maximum-number-of-string-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        for i, w in enumerate(words):
            for j in range(i + 1, len(words)):
                if w == words[j][::-1]:
                    ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maximumNumberOfStringPairs(words)

    print("\noutput:", serialize(ans))
