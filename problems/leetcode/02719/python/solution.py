# Created by shiyang07ca at 2024/01/16 00:01
# leetgo: dev
# https://leetcode.cn/problems/count-of-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Dynamic Programming


class Solution:
    # 链接：https://leetcode.cn/problems/count-of-integers/solutions/2296043/shu-wei-dp-tong-yong-mo-ban-pythonjavacg-9tuc/
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def calc(high: str) -> int:
            @cache
            def dfs(i: int, s: int, is_limit: bool) -> int:
                if s > max_sum:  # 非法
                    return 0
                if i == len(high):
                    return s >= min_sum
                res = 0
                up = int(high[i]) if is_limit else 9
                for d in range(up + 1):  # 枚举当前数位填 d
                    res += dfs(i + 1, s + d, is_limit and d == up)
                return res

            return dfs(0, 0, True)

        is_num1_good = min_sum <= sum(map(int, num1)) <= max_sum
        return (calc(num2) - calc(num1) + is_num1_good) % 1_000_000_007


# @lc code=end

if __name__ == "__main__":
    num1: str = deserialize("str", read_line())
    num2: str = deserialize("str", read_line())
    min_sum: int = deserialize("int", read_line())
    max_sum: int = deserialize("int", read_line())
    ans = Solution().count(num1, num2, min_sum, max_sum)

    print("\noutput:", serialize(ans))
