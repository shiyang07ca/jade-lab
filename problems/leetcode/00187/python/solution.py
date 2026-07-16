# Created by shiyang07ca at 2023/11/05 12:35
# leetgo: dev
# https://leetcode.cn/problems/repeated-dna-sequences/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        ans = set()
        cnt = set()
        ptr = 0
        while ptr + 9 < n:
            ss = s[ptr : ptr + 10]
            if ss not in cnt:
                cnt.add(ss)
            else:
                ans.add(ss)
            ptr += 1
        return list(ans)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findRepeatedDnaSequences(s)

    print("\noutput:", serialize(ans))
