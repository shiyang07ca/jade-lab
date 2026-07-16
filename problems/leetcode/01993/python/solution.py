# Created by shiyang07ca at 2023/09/23 23:50
# leetgo: dev
# https://leetcode.cn/problems/operations-on-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


class LockingTree:
    # https://leetcode.cn/problems/operations-on-tree/solutions/2455158/python3javacgotypescript-yi-ti-yi-jie-df-1iwe/?envType=daily-question&envId=2023-09-23
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.locked = [-1] * n
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for son, fa in enumerate(parent[1:], 1):
            self.children[fa].append(son)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def dfs(x: int):
            nonlocal find
            for y in self.children[x]:
                if self.locked[y] != -1:
                    self.locked[y] = -1
                    find = True
                dfs(y)

        x = num
        while x != -1:
            if self.locked[x] != -1:
                return False
            x = self.parent[x]

        find = False
        dfs(num)
        if not find:
            return False
        self.locked[num] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    parent: List[int] = deserialize("List[int]", constructor_params[0])
    obj = LockingTree(parent)

    for i in range(1, len(ops)):
        match ops[i]:
            case "lock":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                user: int = deserialize("int", method_params[1])
                ans = serialize(obj.lock(num, user))
                output.append(ans)
            case "unlock":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                user: int = deserialize("int", method_params[1])
                ans = serialize(obj.unlock(num, user))
                output.append(ans)
            case "upgrade":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                user: int = deserialize("int", method_params[1])
                ans = serialize(obj.upgrade(num, user))
                output.append(ans)

    print("\noutput:", join_array(output))
