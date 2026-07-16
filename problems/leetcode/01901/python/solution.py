# Created by shiyang07ca at 2023/12/19 00:09
# leetgo: dev
# https://leetcode.cn/problems/find-a-peak-element-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # https://leetcode.cn/problems/find-a-peak-element-ii/solutions/2571587/tu-jie-li-yong-xing-zui-da-zhi-pan-duan-r4e0n/
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat) - 2
        while left <= right:
            i = (left + right) // 2
            mx = max(mat[i])
            if mx > mat[i + 1][mat[i].index(mx)]:
                right = i - 1  # 峰顶行号 <= i
            else:
                left = i + 1  # 峰顶行号 > i
        i = left
        return [i, mat[i].index(max(mat[i]))]


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findPeakGrid(mat)

    print("\noutput:", serialize(ans))
