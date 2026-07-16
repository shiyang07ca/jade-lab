# Created by shiyang07ca at 2024/03/31 21:03
# leetgo: dev
# https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for c in preorder.split(","):
            stk.append(c)
            while len(stk) > 2 and stk[-1] == stk[-2] == "#" and stk[-3] != "#":
                stk = stk[:-3]
                stk.append("#")
        return len(stk) == 1 and stk[0] == "#"

    # 链接：https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/solutions/651132/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/
    def isValidSerialization(self, preorder):
        nodes = preorder.split(",")
        diff = 0
        for node in nodes:
            diff -= 1
            if diff < -1:
                return False
            if node != "#":
                diff += 2
        return diff == -1


# @lc code=end

if __name__ == "__main__":
    preorder: str = deserialize("str", read_line())
    ans = Solution().isValidSerialization(preorder)

    print("\noutput:", serialize(ans))
