# Created by shiyang07ca at 2023/09/30 23:52
# leetgo: dev
# https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/description/
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = days = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda z: -z[1]):
            days += p  # 累加播种天数
            ans = max(ans, days + g)  # 再加上生长天数，就是这个种子的开花时间
        return ans


# @lc code=end

if __name__ == "__main__":
    plantTime: List[int] = deserialize("List[int]", read_line())
    growTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().earliestFullBloom(plantTime, growTime)

    print("\noutput:", serialize(ans))
