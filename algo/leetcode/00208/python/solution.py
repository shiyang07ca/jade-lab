# Created by shiyang07ca at 2026/09/19 13:02
# leetgo: 1.4.17
# https://leetcode.cn/problems/implement-trie-prefix-tree/

from typing import *

from leetgo_py import *

# @lc code=begin


class Trie:
    def __init__(self):
        self.is_leaf = False
        self.next = dict()

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.next:
                cur.next[c] = Trie()
            cur = cur.next[c]
        cur.is_leaf = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        return cur.is_leaf

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Trie()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                obj.insert(word)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(word))
                output.append(ans)
            case "startsWith":
                method_params = split_array(params[i])
                prefix: str = deserialize("str", method_params[0])
                ans = serialize(obj.startsWith(prefix))
                output.append(ans)

    print("\noutput:", join_array(output))
