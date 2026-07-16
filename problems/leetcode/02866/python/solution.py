# Created by shiyang07ca at 2023/12/21 21:26
# leetgo: dev
# https://leetcode.cn/problems/beautiful-towers-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Monotonic Stack


class Solution:
    # https://leetcode.cn/problems/beautiful-towers-ii/solutions/2456562/qian-hou-zhui-fen-jie-dan-diao-zhan-pyth-1exe/?envType=daily-question&envId=2023-12-21
    def maximumSumOfHeights1(self, a: List[int]) -> int:
        n = len(a)
        suf = [0] * (n + 1)
        st = [n]  # 哨兵
        s = 0
        for i in range(n - 1, -1, -1):
            x = a[i]
            while len(st) > 1 and x <= a[st[-1]]:
                j = st.pop()
                s -= a[j] * (st[-1] - j)  # 撤销之前加到 s 中的
            s += x * (st[-1] - i)  # 从 i 到 st[-1]-1 都是 x
            suf[i] = s
            st.append(i)

        ans = s
        st = [-1]  # 哨兵
        pre = 0
        for i, x in enumerate(a):
            while len(st) > 1 and x <= a[st[-1]]:
                j = st.pop()
                pre -= a[j] * (j - st[-1])  # 撤销之前加到 pre 中的
            pre += x * (i - st[-1])  # 从 st[-1]+1 到 i 都是 x
            ans = max(ans, pre + suf[i + 1])
            st.append(i)
        return ans

    def maximumSumOfHeights(self, a):
        n = len(a)

        def get(a):
            f = [0] * n
            st = []
            for i, v in enumerate(a):
                while st and v < a[st[-1]]:
                    st.pop()
                if st:
                    f[i] = f[st[-1]] + (i - st[-1]) * v
                else:
                    f[i] = v * (i + 1)
                st.append(i)
            return f

        pre = get(a)
        suf = get(a[::-1])[::-1]
        return max(x + y - z for x, y, z in zip(pre, suf, a))


# @lc code=end

if __name__ == "__main__":
    maxHeights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSumOfHeights(maxHeights)

    print("\noutput:", serialize(ans))
