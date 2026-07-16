# Created by shiyang07ca at 2023/06/21 00:00
# https://leetcode.cn/problems/fHi6rV/

"""
LCP 41. 黑白翻转棋 (Medium)
在 \`n\*m\` 大小的棋盘中，有黑白两种棋子，黑棋记作字母 \`"X"\`, 白棋记作字母 \`"O"\`，空余位置记作 \
`"."\`。当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋
子，则可以翻转这些棋子的颜色。

!\[1.gif\](https://pic.leetcode-cn.com/1630396029-eTgzpN-6da662e67368466a96d203f67bb6e793.gif){:heig
ht=170px}!\[2.gif\](https://pic.leetcode-cn.com/1630396240-nMvdcc-8e4261afe9f60e05a4f740694b439b6b.g
if){:height=170px}!\[3.gif\](https://pic.leetcode-cn.com/1630396291-kEtzLL-6fcb682daeecb5c3f56eb88b2
3c81d33.gif){:height=170px}

「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 \`chessboard\
`。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。

\\*\\*注意：\\*\\*
\- 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 \\*\\*继续\\*\\* 翻转白棋
\- 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置

\*\*示例 1：\*\*
\> 输入：\`chessboard = \["....X.","....X.","XOOO..","......","......"\]\`
>
\> 输出：\`3\`
>
> 解释：
\> 可以选择下在 \`\[2,4\]\` 处，能够翻转白方三枚棋子。

\*\*示例 2：\*\*
\> 输入：\`chessboard = \[".X.",".O.","XO."\]\`
>
\> 输出：\`2\`
>
> 解释：
\> 可以选择下在 \`\[2,2\]\` 处，能够翻转白方两枚棋子。
!\[2126c1d21b1b9a9924c639d449cc6e65.gif\](https://pic.leetcode-cn.com/1626683255-OBtBud-2126c1d21b1b
9a9924c639d449cc6e65.gif)

\*\*示例 3：\*\*
\> 输入：\`chessboard = \[".......",".......",".......","X......",".O.....","..O....","....OOX"\]\`
>
\> 输出：\`4\`
>
> 解释：
\> 可以选择下在 \`\[6,3\]\` 处，能够翻转白方四枚棋子。
!\[803f2f04098b6174397d6c696f54d709.gif\](https://pic.leetcode-cn.com/1630393770-Puyked-803f2f04098b
6174397d6c696f54d709.gif)

\\*\\*提示：\\*\\*
\- \`1 <= chessboard.length, chessboard\[i\].length <= 8\`
\- \`chessboard\[i\]\` 仅包含 \`"."、"O"\` 和 \`"X"\`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: BFS


# 链接：https://leetcode.cn/problems/fHi6rV/solutions/2315762/python3javacgo-yi-ti-yi-jie-bfs-by-lcbin-e4vo/
class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        def bfs(i: int, j: int) -> int:
            q = deque([(i, j)])
            g = [list(row) for row in chessboard]
            g[i][j] = "X"
            cnt = 0
            while q:
                i, j = q.popleft()
                for a, b in dirs:
                    x, y = i + a, j + b
                    while 0 <= x < m and 0 <= y < n and g[x][y] == "O":
                        x, y = x + a, y + b
                    if 0 <= x < m and 0 <= y < n and g[x][y] == "X":
                        x, y = x - a, y - b
                        cnt += max(abs(x - i), abs(y - j))
                        while x != i or y != j:
                            g[x][y] = "X"
                            q.append((x, y))
                            x, y = x - a, y - b
            return cnt

        m, n = len(chessboard), len(chessboard[0])
        dirs = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a != 0 or b != 0]
        return max(
            bfs(i, j) for i in range(m) for j in range(n) if chessboard[i][j] == "."
        )


# @lc code=end

if __name__ == "__main__":
    chessboard: List[str] = deserialize("List[str]", read_line())
    ans = Solution().flipChess(chessboard)

    print("\noutput:", serialize(ans))
