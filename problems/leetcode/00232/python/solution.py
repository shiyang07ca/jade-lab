# Created by shiyang07ca at 2024/03/04 00:04
# leetgo: dev
# https://leetcode.cn/problems/implement-queue-using-stacks/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# 链接：https://leetcode.cn/problems/implement-queue-using-stacks/solutions/2666136/python3javacgotypescript-yi-ti-yi-jie-sh-sbn3/
class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        self.move()
        return self.stk2.pop()

    def peek(self) -> int:
        self.move()
        return self.stk2[-1]

    def empty(self) -> bool:
        return not self.stk1 and not self.stk2

    def move(self):
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyQueue()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                x: int = deserialize("int", method_params[0])
                obj.push(x)
                output.append("null")
            case "pop":
                ans = serialize(obj.pop())
                output.append(ans)
            case "peek":
                ans = serialize(obj.peek())
                output.append(ans)
            case "empty":
                ans = serialize(obj.empty())
                output.append(ans)

    print("\noutput:", join_array(output))
