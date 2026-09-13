from __future__ import annotations

# Created by shiyang07ca at 2024/04/15 00:00
# leetgo: dev
# https://leetcode.cn/problems/design-hashmap/
from leetgo_py import deserialize, join_array, read_line, serialize, split_array

# @lc code=begin


class MyHashMap:
    def __init__(self):
        self.list: list[int] = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.list[key] = value

    def get(self, key: int) -> int:
        return self.list[key]

    def remove(self, key: int) -> None:
        self.list[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# @lc code=end

if __name__ == "__main__":
    ops: list[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyHashMap()

    for i in range(1, len(ops)):
        match ops[i]:
            case "put":
                method_params = split_array(params[i])
                put_key: int = deserialize("int", method_params[0])
                value: int = deserialize("int", method_params[1])
                obj.put(put_key, value)
                output.append("null")
            case "get":
                method_params = split_array(params[i])
                get_key: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(get_key))
                output.append(ans)
            case "remove":
                method_params = split_array(params[i])
                remove_key: int = deserialize("int", method_params[0])
                obj.remove(remove_key)
                output.append("null")

    print("\noutput:", join_array(output))
