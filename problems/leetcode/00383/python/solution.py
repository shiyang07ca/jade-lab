# Created by shiyang07ca at 2024/01/07 21:55
# leetgo: dev
# https://leetcode.cn/problems/ransom-note/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for r in ransomNote:
            count[r] -= 1
            if count[r] < 0:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    ransomNote: str = deserialize("str", read_line())
    magazine: str = deserialize("str", read_line())
    ans = Solution().canConstruct(ransomNote, magazine)

    print("\noutput:", serialize(ans))
