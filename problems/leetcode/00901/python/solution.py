# Created by shiyang07ca at 2023/10/07 00:02
# leetgo: dev
# https://leetcode.cn/problems/online-stock-span/

import bisect
from typing import *
from leetgo_py import *

# @lc code=begin


# TODO:
# tag: monotonic stack


class StockSpanner:
    def __init__(self):
        self.cur_day = -1
        self.st = [(-1, inf)]

    def next(self, price: int) -> int:
        while price >= self.st[-1][1]:
            self.st.pop()

        self.cur_day += 1
        ans = self.cur_day - self.st[-1][0]
        self.st.append((self.cur_day, price))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = StockSpanner()

    for i in range(1, len(ops)):
        match ops[i]:
            case "next":
                method_params = split_array(params[i])
                price: int = deserialize("int", method_params[0])
                ans = serialize(obj.next(price))
                output.append(ans)

    print("\noutput:", join_array(output))
