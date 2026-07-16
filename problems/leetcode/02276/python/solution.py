# Created by shiyang07ca at 2023/12/16 11:43
# leetgo: dev
# https://leetcode.cn/problems/count-integers-in-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# https://leetcode.cn/problems/count-integers-in-intervals/solutions/1495396/by-endlesscheng-clk2/?envType=daily-question&envId=2023-12-16
class CountIntervals:
    __slots__ = "left", "right", "l", "r", "cnt"

    def __init__(self, l=1, r=10**9):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.cnt == self.r - self.l + 1:
            return  # self 已被完整覆盖，无需执行任何操作
        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.cnt = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2
        if self.left is None:
            self.left = CountIntervals(self.l, mid)  # 动态开点
        if self.right is None:
            self.right = CountIntervals(mid + 1, self.r)  # 动态开点
        if l <= mid:
            self.left.add(l, r)
        if mid < r:
            self.right.add(l, r)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = CountIntervals()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.add(left, right)
                output.append("null")
            case "count":
                ans = serialize(obj.count())
                output.append(ans)

    print("\noutput:", join_array(output))
