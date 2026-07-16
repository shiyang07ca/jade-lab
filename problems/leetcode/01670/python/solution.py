# Created by shiyang07ca at 2023/11/28 20:54
# leetgo: dev
# https://leetcode.cn/problems/design-front-middle-back-queue/

from typing import *
from leetgo_py import *

# @lc code=begin


# 链接：https://leetcode.cn/problems/design-front-middle-back-queue/
class FrontMiddleBackQueue:
    __slots__ = "left", "right"

    def __init__(self):
        self.left = deque()
        self.right = deque()

    # 调整长度，保证 0 <= len(right) - len(left) <= 1
    # 从而保证可以在正中间插入删除元素
    def balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.right:  # 整个队列为空
            return -1
        val = self.left.popleft() if self.left else self.right.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.right:  # 整个队列为空
            return -1
        if len(self.left) == len(self.right):
            return self.left.pop()
        return self.right.popleft()

    def popBack(self) -> int:
        if not self.right:  # 整个队列为空
            return -1
        val = self.right.pop()
        self.balance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FrontMiddleBackQueue()

    for i in range(1, len(ops)):
        match ops[i]:
            case "pushFront":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushFront(val)
                output.append("null")
            case "pushMiddle":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushMiddle(val)
                output.append("null")
            case "pushBack":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushBack(val)
                output.append("null")
            case "popFront":
                ans = serialize(obj.popFront())
                output.append(ans)
            case "popMiddle":
                ans = serialize(obj.popMiddle())
                output.append(ans)
            case "popBack":
                ans = serialize(obj.popBack())
                output.append(ans)

    print("\noutput:", join_array(output))
