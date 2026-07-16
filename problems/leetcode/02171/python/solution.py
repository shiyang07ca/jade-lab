# Created by shiyang07ca at 2024/01/18 00:06
# leetgo: dev
# https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumRemoval1(self, beans: List[int]) -> int:
        beans.sort()
        pre = list(accumulate(beans, initial=0))
        suf = list(accumulate(beans[::-1], initial=0))
        ans = inf
        n = len(beans)
        for i, x in enumerate(beans):
            c = 0
            if i > 0:
                c += pre[i]
            if i < n - 1:
                c += suf[n - i - 1] - x * (n - i - 1)
            ans = min(ans, c)

        return ans

    # 链接：https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/solutions/1262419/pai-xu-hou-yi-ci-bian-li-by-endlesscheng-36g8/
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        return sum(beans) - max((len(beans) - i) * v for i, v in enumerate(beans))


# @lc code=end

if __name__ == "__main__":
    beans: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRemoval(beans)

    print("\noutput:", serialize(ans))
