# Created by shiyang07ca at 2024/04/14 12:56
# leetgo: dev
# https://leetcode.cn/problems/design-hashset/

from typing import *
from leetgo_py import *

# @lc code=begin


class MyHashSet:
    def __init__(self):
        self.list = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.list[key] = True

    def remove(self, key: int) -> None:
        self.list[key] = False

    def contains(self, key: int) -> bool:
        return self.list[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyHashSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.add(key)
                output.append("null")
            case "remove":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.remove(key)
                output.append("null")
            case "contains":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.contains(key))
                output.append(ans)

    print("\noutput:", join_array(output))
