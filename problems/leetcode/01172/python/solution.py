# Created by shiyang07ca at 2023/04/28 23:31
# https://leetcode.cn/problems/dinner-plate-stacks/

"""
1172. 餐盘栈 (Hard)
我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号
。每个栈的的最大容量 `capacity` 都相同。

实现一个叫「餐盘」的类 `DinnerPlates`：

- `DinnerPlates(int capacity)` \- 给出栈的最大容量 `capacity
`。
- `void push(int val)` \- 将给出的正整数 `val` 推入 **从左往
右第一个** 没有满的栈。
- `int pop()` \- 返回 **从右往左第一个** 非空栈顶部的值，并
将其从栈中删除；如果所有的栈都是空的，请返回 `-1`。
- `int popAtStack(int index)` \- 返回编号 `index` 的栈顶部的
值，并将其从栈中删除；如果编号 `index` 的栈是空的，请返回 `-
1`。

**示例：**

```
输入：
["DinnerPlates","push","push","push","push","push","popAtSta
ck","push","push","popAtStack","popAtStack","pop","pop","pop
","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[
]]
输出：
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

解释：
DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 cap
acity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // 栈的现状为：    2  4
                                    1  3  5
                                    ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 2。栈的现状为：      4
                                          1  3  5
                                          ﹈ ﹈ ﹈
D.push(20);        // 栈的现状为：  20  4
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.push(21);        // 栈的现状为：  20  4 21
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.popAtStack(2);   // 返回 21。栈的现状为：       4
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.pop()            // 返回 5。栈的现状为：        4
                                            1  3
                                            ﹈ ﹈
D.pop()            // 返回 4。栈的现状为：    1  3
                                           ﹈ ﹈
D.pop()            // 返回 3。栈的现状为：    1
                                           ﹈
D.pop()            // 返回 1。现在没有栈。
D.pop()            // 返回 -1。仍然没有栈。

```

**提示：**

- `1 <= capacity <= 20000`
- `1 <= val <= 20000`
- `0 <= index <= 100000`
- 最多会对 `push`， `pop`，和 `popAtStack` 进行 `200000` 次
调用。

"""

from typing import *
from leetgo_py import *

# @lc code=begin

from heapq import *


class DinnerPlates:
    def __init__(self, capacity: int):
        self.c = capacity
        self.s = []
        self.h = []

    def push(self, val: int) -> None:
        s = self.s
        if s:
            if self.h:
                i = heappop(self.h)
                if i < len(s) and len(s[i]) < self.c:
                    s[i].append(val)
                    return
            if len(s[-1]) == self.c:
                s.append([val])
            else:
                s[-1].append(val)
        else:
            s.append([val])

    def pop(self) -> int:
        s = self.s
        if s:
            while len(s) and not s[-1]:
                s.pop()
            if not s:
                return -1
            else:
                return s[-1].pop()
        return -1

    def popAtStack(self, i: int) -> int:
        s = self.s
        if i < len(s):
            if s[i]:
                heappush(self.h, i)
                return self.s[i].pop()
            else:
                return -1
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    capacity: int = deserialize("int", constructor_params[0])
    obj = DinnerPlates(capacity)

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.push(val)
                output.append("null")
            case "pop":
                ans = serialize(obj.pop())
                output.append(ans)
            case "popAtStack":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                ans = serialize(obj.popAtStack(index))
                output.append(ans)

    print("output: " + join_array(output))
