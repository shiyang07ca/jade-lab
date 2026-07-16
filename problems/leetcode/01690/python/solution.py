# Created by shiyang07ca at 2024/02/03 14:40
# leetgo: dev
# https://leetcode.cn/problems/stone-game-vii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Dynamic Programming


class Solution:
    # 链接：https://leetcode.cn/problems/stone-game-vii/solutions/2629582/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-zktx/
    def stoneGameVII(self, stones: List[int]) -> int:
        s = list(accumulate(stones, initial=0))  # 前缀和

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == j:  # 递归边界
                return 0
            a = s[j + 1] - s[i + 1] - dfs(i + 1, j)
            b = s[j] - s[i] - dfs(i, j - 1)
            return max(a, b)

        ans = dfs(0, len(stones) - 1)
        dfs.cache_clear()  # 防止爆内存
        return ans


# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVII(stones)

    print("\noutput:", serialize(ans))
