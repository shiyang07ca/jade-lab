# Created by shiyang07ca at 2024/02/05 00:54
# leetgo: dev
# https://leetcode.cn/problems/jump-game-vi/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Monotonic Queue


class Solution:
    # 链接：https://leetcode.cn/problems/jump-game-vi/solutions/2631981/yi-bu-bu-you-hua-cong-di-gui-dao-di-tui-84qn3/
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        q = deque([0])
        for i in range(1, n):
            # 1. 出
            if q[0] < i - k:
                q.popleft()
            # 2. 转移
            f[i] = f[q[0]] + nums[i]
            # 3. 入
            while q and f[i] >= f[q[-1]]:
                q.pop()
            q.append(i)
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxResult(nums, k)

    print("\noutput:", serialize(ans))
