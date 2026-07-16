# Created by shiyang07ca at 2024/06/06 21:58
# leetgo: dev
# https://leetcode.cn/problems/separate-black-and-white-balls/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt1 = ans = 0
        for i, x in enumerate(s):
            if x == "0":
                ans += cnt1
            else:
                cnt1 += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumSteps(s)
    print("\noutput:", serialize(ans, "long"))
