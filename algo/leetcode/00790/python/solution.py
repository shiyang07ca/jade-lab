# Created by shiyang07ca at 2026/10/13 23:34
# leetgo: 1.4.17
# https://leetcode.cn/problems/domino-and-tromino-tiling/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        # full[i]：铺满 2 × i 完整面板的方法数。
        # gap[i]：铺满 2 × i 面板去掉右上角后的方法数。
        # 去掉右下角的方案数相同，但不重复计入 gap[i]。
        full = [0] * (n + 1)
        gap = [0] * (n + 1)
        full[0] = 1  # 空面板有一种铺法：什么都不放。
        full[1] = 1  # 一块竖向多米诺；缺角时只剩一格，gap[1] = 0。

        for i in range(2, n + 1):
            # 右下角用横向多米诺覆盖，或用一块 L 形瓷砖覆盖。
            gap[i] = (gap[i - 1] + full[i - 2]) % mod

            # 右端：竖向多米诺、两块横向多米诺、两种朝向的 L 形瓷砖。
            full[i] = (
                full[i - 1] + full[i - 2] + 2 * gap[i - 1]
            ) % mod

        return full[n]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numTilings(n)
    print("\noutput:", serialize(ans, "integer"))
