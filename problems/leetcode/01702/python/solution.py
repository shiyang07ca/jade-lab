# Created by shiyang07ca at 2024/04/10 21:25
# leetgo: dev
# https://leetcode.cn/problems/maximum-binary-string-after-change/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Greedy


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-binary-string-after-change/solutions/2732155/tan-xin-jian-ji-xie-fa-pythonjavacgojsru-szie/
    def maximumBinaryString(self, binary: str) -> str:
        i = binary.find("0")
        if i < 0:  # binary 全是 '1'
            return binary
        cnt1 = binary.count("1", i)  # 统计 binary[i:] 中 '1' 的个数
        return "1" * (len(binary) - 1 - cnt1) + "0" + "1" * cnt1


# @lc code=end

if __name__ == "__main__":
    binary: str = deserialize("str", read_line())
    ans = Solution().maximumBinaryString(binary)
    print("\noutput:", serialize(ans, "string"))
