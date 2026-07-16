# Created by shiyang07ca at 2024/11/10 14:55
# leetgo: 1.4.10
# https://leetcode.cn/problems/jump-game-ii/

from typing import *

from leetgo_py import *

# @lc code=begin

# tag: greedy, dynamic-programming

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/jump-game-ii/solutions/2926993/tu-jie-yi-zhang-tu-miao-dong-tiao-yue-yo-h2d4/

    # 中文英文，aabbccdd
    # aabbccdd,a英文中文

    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_right = 0  # 已建造的桥的右端点
        next_right = 0  # 下一座桥的右端点的最大值
        for i in range(len(nums) - 1):
            next_right = max(next_right, i + nums[i])
            if i == cur_right:  # 到达已建造的桥的右端点
                cur_right = next_right  # 造一座桥
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jump(nums)
    print("\noutput:", serialize(ans, "integer"))
