# Created by shiyang07ca at 2024/06/11 00:15
# leetgo: dev
# https://leetcode.cn/problems/battleships-in-a-board/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/battleships-in-a-board/solutions/1162182/jia-ban-shang-de-zhan-jian-by-leetcode-s-kxpc/
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == "X":
                    row[j] = "."
                    for k in range(j + 1, n):
                        if row[k] != "X":
                            break
                        row[k] = "."
                    for k in range(i + 1, m):
                        if board[k][j] != "X":
                            break
                        board[k][j] = "."
                    ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().countBattleships(board)
    print("\noutput:", serialize(ans, "integer"))
