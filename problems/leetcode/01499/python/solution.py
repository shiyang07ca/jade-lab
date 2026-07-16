# Created by shiyang07ca at 2023/07/21 12:42
# leetgo: dev
# https://leetcode.cn/problems/max-value-of-equation/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: Monotonic Queue


class Solution:
    # 链接：https://leetcode.cn/problems/max-value-of-equation/solutions/2352457/on-dan-diao-dui-lie-fu-ti-dan-pythonjava-hhrr/
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -inf
        q = deque()
        for x, y in points:
            while q and q[0][0] < x - k:  # 队首超出范围
                q.popleft()  # 弹它！
            if q:
                ans = max(ans, x + y + q[0][1])  # 加上最大的 yi-xi
            while q and q[-1][1] <= y - x:  # 队尾不如新来的强
                q.pop()  # 弹它！
            q.append((x, y - x))
        return ans


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaxValueOfEquation(points, k)

    print("\noutput:", serialize(ans))
