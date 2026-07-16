# Created by shiyang07ca at 2024/02/01 21:56
# leetgo: dev
# https://leetcode.cn/problems/5TxKeK/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

class Solution:
    # 链接：https://leetcode.cn/problems/5TxKeK/solutions/2627350/zhuan-huan-zhong-wei-shu-tan-xin-dui-din-7r9b/
    def numsGame(self, nums: List[int]) -> List[int]:
        MOD = 1_000_000_007
        ans = [0] * len(nums)
        left = []   # 维护较小的一半，大根堆（小根堆取负号）
        right = []  # 维护较大的一半，小根堆
        left_sum = right_sum = 0
        for i, b in enumerate(nums):
            b -= i
            if i % 2 == 0:  # 前缀长度是奇数
                left_sum -= max(-left[0] - b, 0) if left else 0
                t = -heappushpop(left, -b)
                right_sum += t
                heappush(right, t)
                ans[i] = (right_sum - right[0] - left_sum) % MOD
            else:  # 前缀长度是偶数
                right_sum += max(b - right[0], 0)
                t = heappushpop(right, b)
                left_sum += t
                heappush(left, -t)
                ans[i] = (right_sum - left_sum) % MOD
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numsGame(nums)

    print("\noutput:", serialize(ans))
