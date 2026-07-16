# Created by shiyang07ca at 2023/11/30 22:26
# leetgo: dev
# https://leetcode.cn/problems/determine-if-two-strings-are-close/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        if (
            len(word1) != len(word2)
            or set(cnt1.keys()) != set(cnt2.keys())
            or sorted(cnt1.values()) != sorted(cnt2.values())
        ):
            return False

        return True


# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().closeStrings(word1, word2)

    print("\noutput:", serialize(ans))
