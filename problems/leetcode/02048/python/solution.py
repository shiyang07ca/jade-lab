# Created by shiyang07ca at 2023/12/09 10:55
# leetgo: dev
# https://leetcode.cn/problems/next-greater-numerically-balanced-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/next-greater-numerically-balanced-number/
    def nextBeautifulNumber(self, n: int) -> int:
        for x in count(n + 1):
            y = x
            cnt = [0] * 10
            while y:
                y, v = divmod(y, 10)
                cnt[v] += 1
            if all(v == 0 or i == v for i, v in enumerate(cnt)):
                return x


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().nextBeautifulNumber(n)

    print("\noutput:", serialize(ans))
