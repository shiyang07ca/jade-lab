# Created by shiyang07ca at 2024/03/21 08:29
# leetgo: dev
# https://leetcode.cn/problems/frequency-tracker/

from typing import *
from leetgo_py import *

# @lc code=begin


class FrequencyTracker:
    def __init__(self):
        self.cnt = Counter()
        self.fq = Counter()

    def add(self, n: int) -> None:
        self.fq[self.cnt[n]] -= 1
        self.cnt[n] += 1
        self.fq[self.cnt[n]] += 1

    def deleteOne(self, n: int) -> None:
        if self.cnt[n] == 0:
            return
        self.fq[self.cnt[n]] -= 1
        self.cnt[n] -= 1
        self.fq[self.cnt[n]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.fq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FrequencyTracker()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                number: int = deserialize("int", method_params[0])
                obj.add(number)
                output.append("null")
            case "deleteOne":
                method_params = split_array(params[i])
                number: int = deserialize("int", method_params[0])
                obj.deleteOne(number)
                output.append("null")
            case "hasFrequency":
                method_params = split_array(params[i])
                frequency: int = deserialize("int", method_params[0])
                ans = serialize(obj.hasFrequency(frequency))
                output.append(ans)

    print("\noutput:", join_array(output))
