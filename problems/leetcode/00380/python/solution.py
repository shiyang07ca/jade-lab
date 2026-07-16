# Created by shiyang07ca at 2025/02/03 09:57
# leetgo: 1.4.13
# https://leetcode.cn/problems/insert-delete-getrandom-o1/

from typing import *

from leetgo_py import *

# TODO:
# tag: hash, array, design

# @lc code=begin


class RandomizedSet:
    # https://leetcode.cn/problems/insert-delete-getrandom-o1/solutions/1416888/by-ac_oier-tpex/?envType=study-plan-v2&envId=top-interview-150
    def __init__(self):
        self.nums = [0] * 200010
        self.map = {}
        self.idx = -1

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.idx += 1
        self.nums[self.idx] = val
        self.map[val] = self.idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        loc = self.map.pop(val)
        idx_val = self.nums[self.idx]
        if loc != self.idx:
            self.map[idx_val] = loc
        self.nums[loc] = idx_val
        self.idx -= 1

        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, self.idx)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = RandomizedSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                ans = serialize(obj.insert(val))
                output.append(ans)
            case "remove":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                ans = serialize(obj.remove(val))
                output.append(ans)
            case "getRandom":
                ans = serialize(obj.getRandom())
                output.append(ans)

    print("\noutput:", join_array(output))
