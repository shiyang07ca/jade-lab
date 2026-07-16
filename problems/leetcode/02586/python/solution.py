# Created by shiyang07ca at 2023/11/07 13:26
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ["a", "e", "i", "o", "u"]
        return sum(
            1 for w in words[left : right + 1] if w[0] in vowel and w[-1] in vowel
        )


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().vowelStrings(words, left, right)

    print("\noutput:", serialize(ans))
