from __future__ import annotations

# Created by shiyang07ca at 2024/01/04 00:00
# leetgo: dev
# https://leetcode.cn/problems/maximum-rows-covered-by-columns/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-rows-covered-by-columns/solutions/1798794/by-endlesscheng-dvxe/
    def maximumRows(self, mat: list[list[int]], numSelect: int) -> int:
        mask = [sum(x << j for j, x in enumerate(row)) for i, row in enumerate(mat)]
        ans = 0
        for subset in range(1 << len(mat[0])):
            if subset.bit_count() == numSelect:  # subset 的大小等于 numSelect
                covered_rows = sum(row & subset == row for row in mask)
                ans = max(ans, covered_rows)
        return ans


# @lc code=end

if __name__ == "__main__":
    matrix: list[list[int]] = deserialize("List[List[int]]", read_line())
    numSelect: int = deserialize("int", read_line())
    ans = Solution().maximumRows(matrix, numSelect)

    print("\noutput:", serialize(ans))
