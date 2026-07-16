# Created by shiyang07ca at 2024/04/26 00:17
# leetgo: dev
# https://leetcode.cn/problems/snapshot-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class SnapshotArray:
    # 链接：https://leetcode.cn/problems/snapshot-array/solutions/18730/ha-xi-zi-dian-er-fen-cha-zhao-python3-by-smoon1989/
    def __init__(self, length: int):
        # 初始化字典数组和 id
        self.arr = [{0: 0} for _ in range(length)]
        self.sid = 0

    def set(self, index: int, val: int) -> None:
        # 设置当前快照的元素值
        self.arr[index][self.sid] = val

    def snap(self) -> int:
        # 每次快照 id 加 1
        self.sid += 1
        # 返回上一个快照 id
        return self.sid - 1

    def get(self, index: int, snap_id: int) -> int:
        # 选择要查找的元素的字典
        d = self.arr[index]
        # 如果快照恰好存在, 直接返回
        if snap_id in d:
            return d[snap_id]
        # 不存在则进行二分搜索, 查找快照前最后一次修改
        k = list(d.keys())
        i = bisect.bisect_left(k, snap_id)
        return d[k[i - 1]]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    length: int = deserialize("int", constructor_params[0])
    obj = SnapshotArray(length)

    for i in range(1, len(ops)):
        match ops[i]:
            case "set":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.set(index, val)
                output.append("null")
            case "snap":
                ans = serialize(obj.snap())
                output.append(ans)
            case "get":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                snap_id: int = deserialize("int", method_params[1])
                ans = serialize(obj.get(index, snap_id))
                output.append(ans)

    print("\noutput:", join_array(output))
