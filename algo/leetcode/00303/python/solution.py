from __future__ import annotations

from itertools import accumulate

# Created by shiyang07ca at 2024/03/18 00:03
# leetgo: dev
# https://leetcode.cn/problems/range-sum-query-immutable/
from leetgo_py import deserialize, join_array, read_line, serialize, split_array

# @lc code=begin


class NumArray:
    def __init__(self, nums: list[int]):
        self.acc = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right + 1] - self.acc[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# @lc code=end

if __name__ == "__main__":
    ops: list[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums: list[int] = deserialize("List[int]", constructor_params[0])
    _ = deserialize("int", constructor_params[1])
    obj = NumArray(nums)

    for i in range(1, len(ops)):
        match ops[i]:
            case "sumRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                ans = serialize(obj.sumRange(left, right))
                output.append(ans)

    print("\noutput:", join_array(output))
