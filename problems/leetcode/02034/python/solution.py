# Created by shiyang07ca at 2023/10/08 00:05
# leetgo: dev
# https://leetcode.cn/problems/stock-price-fluctuation/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

from sortedcontainers import SortedList


# 链接：https://leetcode.cn/problems/stock-price-fluctuation/
class StockPrice:
    def __init__(self):
        self.d = {}
        self.ls = SortedList()
        self.last = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.d:
            self.ls.remove(self.d[timestamp])
        self.d[timestamp] = price
        self.ls.add(price)
        self.last = max(self.last, timestamp)

    def current(self) -> int:
        return self.d[self.last]

    def maximum(self) -> int:
        return self.ls[-1]

    def minimum(self) -> int:
        return self.ls[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = StockPrice()

    for i in range(1, len(ops)):
        match ops[i]:
            case "update":
                method_params = split_array(params[i])
                timestamp: int = deserialize("int", method_params[0])
                price: int = deserialize("int", method_params[1])
                obj.update(timestamp, price)
                output.append("null")
            case "current":
                ans = serialize(obj.current())
                output.append(ans)
            case "maximum":
                ans = serialize(obj.maximum())
                output.append(ans)
            case "minimum":
                ans = serialize(obj.minimum())
                output.append(ans)

    print("\noutput:", join_array(output))
