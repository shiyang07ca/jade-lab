# Created by shiyang07ca at 2023/08/02 09:42
# leetgo: dev
# https://leetcode.cn/problems/card-flipping-game/

from typing import *
from math import *

from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    # 链接：https://leetcode.cn/problems/card-flipping-game/solutions/2368863/yue-du-li-jie-ti-pythonjavacgojs-by-endl-ze7f/
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        forbidden = {x for x, y in zip(fronts, backs) if x == y}
        return min((x for x in fronts + backs if x not in forbidden), default=0)


# @lc code=end

if __name__ == "__main__":
    fronts: List[int] = deserialize("List[int]", read_line())
    backs: List[int] = deserialize("List[int]", read_line())
    ans = Solution().flipgame(fronts, backs)

    print("\noutput:", serialize(ans))
