# Created by shiyang07ca at 2024/05/19 00:06
# leetgo: dev
# https://leetcode.cn/problems/find-the-winner-of-an-array-game/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-the-winner-of-an-array-game/solutions/2773465/mo-ni-fu-ruo-gan-jin-jie-wen-ti-pythonja-zx17/
    def getWinner(self, arr: List[int], k: int) -> int:
        mx = arr[0]
        win = -1  # 对于 arr[0] 来说，需要连续 k+1 个回合都是最大值
        for x in arr:
            if x > mx:  # 新的最大值
                mx = x
                win = 0
            win += 1  # 获胜回合 +1
            if win == k:
                break
        return mx


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getWinner(arr, k)
    print("\noutput:", serialize(ans, "integer"))
