# Created by shiyang07ca at 2023/10/23 10:13
# leetgo: dev
# https://leetcode.cn/problems/number-of-senior-citizens/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for d in details:
            ans += int(d[11:13]) > 60
        return ans


# @lc code=end

if __name__ == "__main__":
    details: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countSeniors(details)

    print("\noutput:", serialize(ans))
