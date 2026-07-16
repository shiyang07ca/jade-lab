# Created by shiyang07ca at 2024/01/08 21:25
# leetgo: dev
# https://leetcode.cn/problems/number-of-boomerangs/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: Hash Table, Math
# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/number-of-boomerangs/solutions/2595488/jian-ji-xie-fa-fu-xiang-si-ti-mu-pythonj-39p8/
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            cnt = Counter()
            for x2, y2 in points:
                d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                ans += cnt[d2] * 2
                cnt[d2] += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfBoomerangs(points)

    print("\noutput:", serialize(ans))
