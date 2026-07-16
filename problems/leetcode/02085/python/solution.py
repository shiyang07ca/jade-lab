# Created by shiyang07ca at 2024/01/12 13:19
# leetgo: dev
# https://leetcode.cn/problems/count-common-words-with-one-occurrence/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1, cnt2 = Counter(words1), Counter(words2)
        ans = 0
        for w, c in cnt1.items():
            if c == 1 and cnt2[w] == 1:
                ans += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    words1: List[str] = deserialize("List[str]", read_line())
    words2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countWords(words1, words2)

    print("\noutput:", serialize(ans))
