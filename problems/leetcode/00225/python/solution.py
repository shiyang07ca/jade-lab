# Created by shiyang07ca at 2024/03/03 10:19
# leetgo: dev
# https://leetcode.cn/problems/implement-stack-using-queues/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# 链接：https://leetcode.cn/problems/implement-stack-using-queues/solutions/2664345/python3javacgo-yi-ti-yi-jie-liang-ge-dui-lt48/
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyStack()

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
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "empty":
                ans = serialize(obj.empty())
                output.append(ans)

    print("\noutput:", join_array(output))
