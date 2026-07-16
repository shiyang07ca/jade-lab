# Created by shiyang07ca at 2023/10/09 00:06
# leetgo: dev
# https://leetcode.cn/problems/split-with-minimum-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/split-with-minimum-sum/
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        return int("".join(s[::2])) + int("".join(s[1::2]))


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().splitNum(num)

    print("\noutput:", serialize(ans))
