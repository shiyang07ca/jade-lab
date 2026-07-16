# Created by shiyang07ca at 2024/01/30 13:47
# leetgo: dev
# https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/solutions/2614614/shi-xun-huan-shu-zu-suo-you-yuan-su-xian-1bfa/
    def minimumSeconds(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        res = n = len(nums)
        for i, a in enumerate(nums):
            mp[a].append(i)
        for pos in mp.values():
            mx = pos[0] + n - pos[-1]
            for i in range(len(pos)):
                mx = max(mx, pos[i] - pos[i - 1])
            res = min(res, mx // 2)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumSeconds(nums)

    print("\noutput:", serialize(ans))
