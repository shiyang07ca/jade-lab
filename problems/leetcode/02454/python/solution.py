# Created by shiyang07ca at 2023/12/12 22:12
# leetgo: dev
# https://leetcode.cn/problems/next-greater-element-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

from sortedcontainers import SortedList


class Solution:
    # 链接：https://leetcode.cn/problems/next-greater-element-iv/solutions/1935877/by-endlesscheng-q6t5/?envType=daily-question&envId=2023-12-12
    def secondGreaterElement1(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s = []
        t = []
        for i, x in enumerate(nums):
            while t and nums[t[-1]] < x:
                ans[t.pop()] = x  # t 栈顶的下下个更大元素是 x
            j = len(s) - 1
            while j >= 0 and nums[s[j]] < x:
                j -= 1  # s 栈顶的下一个更大元素是 x
            t += s[j + 1 :]  # 把从 s 弹出的这一整段元素加到 t
            del s[j + 1 :]  # 弹出一整段元素
            s.append(i)  # 当前元素（的下标）加到 s 栈顶
        return ans

    # https://leetcode.cn/problems/next-greater-element-iv/solutions/2563191/python3javactypescript-yi-ti-yi-jie-pai-sysin/?envType=daily-question&envId=2023-12-12
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        arr = [(x, i) for i, x in enumerate(nums)]
        arr.sort(key=lambda x: -x[0])
        sl = SortedList()
        n = len(nums)
        ans = [-1] * n
        for _, i in arr:
            j = sl.bisect_right(i)
            if j + 1 < len(sl):
                ans[i] = nums[sl[j + 1]]
            sl.add(i)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().secondGreaterElement(nums)

    print("\noutput:", serialize(ans))
