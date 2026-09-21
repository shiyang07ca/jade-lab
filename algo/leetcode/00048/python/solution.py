# Created by shiyang07ca at 2026/09/16 23:44
# leetgo: 1.4.17
# https://leetcode.cn/problems/rotate-image/

from typing import *

from leetgo_py import *

# @lc code=begin


# 链接：https://leetcode.cn/problems/rotate-image/solutions/3655166/shu-xue-ben-zhi-liang-ci-fan-zhuan-deng-aon4a/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 第一步：转置
        for i in range(n):
            for j in range(i):  # 遍历对角线下方元素
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：行翻转
        for row in matrix:
            row.reverse()


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().rotate(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
