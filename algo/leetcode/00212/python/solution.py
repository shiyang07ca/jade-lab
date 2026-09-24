# Created by shiyang07ca at 2026/09/25 01:03
# leetgo: 1.4.17
# https://leetcode.cn/problems/word-search-ii/

from typing import *

from leetgo_py import *

# @lc code=begin


# TODO
class Solution:
    def findWords(self, board, words):
        END = "#"  # 单词结束标记
        root = {}
        for w in words:  # 建树
            node = root
            for ch in w:
                node = node.setdefault(ch, {})
            node[END] = w

        m, n, ans = len(board), len(board[0]), []

        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node:  # 前缀不存在 → 剪枝
                return
            nxt = node[ch]  # 棋盘走一格 = 树走一层
            if END in nxt:  # 命中完整单词
                ans.append(nxt.pop(END))  # 弹出：防止其他路径重复收集
            board[i][j] = ""  # 标记已用（用空串比 "#" 更不易混）
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and board[x][y]:
                    dfs(x, y, nxt)  # 注意：往下传的是 nxt
            board[i][j] = ch  # 回溯：恢复现场
            if not nxt:  # 叶子剪枝
                node.pop(ch)

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return sorted(ans)


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findWords(board, words)
    print("\noutput:", serialize(ans, "string[]"))
