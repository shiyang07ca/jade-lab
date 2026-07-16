# Created by shiyang07ca at 2024/03/27 21:53
# leetgo: dev
# https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/solutions/2147717/tiao-yue-you-xi-bian-xing-by-endlesschen-hatn/
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda p: p[0])
        m, max_r = 0, -1
        for l, r in ranges:
            if l > max_r:  # 无法合并
                m += 1  # 新区间
            max_r = max(max_r, r)  # 合并
        return pow(2, m, 1_000_000_007)


# @lc code=end

if __name__ == "__main__":
    ranges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countWays(ranges)

    print("\noutput:", serialize(ans))
