# Created by shiyang07ca at 2023/11/29 22:50
# leetgo: dev
# https://leetcode.cn/problems/smallest-number-in-infinite-set/

from typing import *
from leetgo_py import *

# @lc code=begin

from sortedcontainers import SortedList


class SmallestInfiniteSet:
    def __init__(self):
        self.set = SortedList([1])

    def popSmallest(self) -> int:
        v = self.set.pop(0)
        if not self.set:
            self.set.add(v + 1)
        return v

    def addBack(self, num: int) -> None:
        if num < self.set[-1] and num not in self.set:
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = SmallestInfiniteSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "popSmallest":
                ans = serialize(obj.popSmallest())
                output.append(ans)
            case "addBack":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addBack(num)
                output.append("null")

    print("\noutput:", join_array(output))
