"""

单调栈 Monotone Stack


https://oi-wiki.org/ds/monotonous-stack/
https://cp-algorithms.com/data_structures/stack_queue_modification.html
https://algo.itcharge.cn/03.Stack/02.Monotone-Stack/01.Monotone-Stack/

模板题
https://www.luogu.com.cn/problem/P5788
https://www.luogu.com.cn/problem/P2866 http://poj.org/problem?id=3250


单调栈可以在时间复杂度为 O(n) 的情况下，求解出某个元素左边或者右边第一个比它大或者小的元素。



满足从栈顶到栈底的元素是单调递增的栈，叫做「单调递增栈」。
满足从栈顶到栈底的元素是单调递减的栈，叫做「单调递减栈」。

单调递增栈：只有比栈顶元素小的元素才能直接进栈，否则需要先将栈中比当前元素小的元素出栈，再将当前元素入栈。


这样就保证了：栈中保留的都是比当前入栈元素大的值，并且从栈顶到栈底的元素值是单调递增的。

单调递增栈的入栈、出栈过程如下：
假设当前进栈元素为 x，如果 x 比栈顶元素小，则直接入栈。
否则从栈顶开始遍历栈中元素，把小于 x 或者等于 x 的元素弹出栈，直到遇到一个大于 x 的元素为止，然后再把 x 压入栈中。



所以单调栈一般用于解决一下几种问题：

- 寻找左侧第一个比当前元素大的元素。
- 寻找左侧第一个比当前元素小的元素。
- 寻找右侧第一个比当前元素大的元素。
- 寻找右侧第一个比当前元素小的元素。


模板题
LC496. 下一个更大元素 I https://leetcode.cn/problems/next-greater-element-i/
LC503. 下一个更大元素 II  https://leetcode.cn/problems/next-greater-element-ii/

练习
LC739. 每日温度  https://leetcode.cn/problems/daily-temperatures/
LC901. 股票价格跨度  https://leetcode.cn/problems/online-stock-span/
LC316. 去除重复字母  https://leetcode.cn/problems/remove-duplicate-letters/
LC1081. 不同字符的最小子序列  https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/


LC42. 接雨水  https://leetcode.cn/problems/trapping-rain-water/
LC84. 柱状图中最大的矩形
LC85. 最大矩形  https://leetcode.cn/problems/maximal-rectangle/


计算贡献
LC907. 子数组的最小值之和 https://leetcode.cn/problems/sum-of-subarray-minimums/
LC2104. 子数组范围和 https://leetcode.cn/problems/sum-of-subarray-minimums/


"""


def monotne_stack(nums):
    st = []
    for n in nums:
        # while st and st[-1] >= num: # 单调递增栈
        while st and st[-1] <= n:  # 单调递减栈，不断弹出 <= n 的，循环结束后栈顶就是 > n 的
            st.pop()
        st.append(n)


"""

* 描述
  给定一个不含有重复值的数组arr，找到每一个i位置左边和右边离i位置最近
  且严格小于/大于 arr[i] 的位置。返回所有位置相应的信息。

* 举例

arr = [3, 4, 1, 5, 6, 2, 7]

返回二维数组
[
  [-1, 2],
  [0, 2],
  [-1, -1],
  [2, 5],
  [3, 5],
  [2, -1],
  [5, -1]
]

* 思路
  维护一个底小顶大的单调栈，入栈时不断比较栈顶元素，直到找到一个比当前元素小的，否则弹出栈顶

"""


# brute force
def get_near_less_no_repeat1(arr):
    if len(arr) == 0:
        return []

    ans = []
    for i, e in enumerate(arr):
        left, right = -1, -1

        cur = i - 1
        while cur >= 0:
            if arr[cur] < e:
                left = cur
                break
            cur -= 1

        cur = i + 1
        while cur < len(arr):
            if arr[cur] < e:
                right = cur
                break
            cur += 1

        ans.append([left, right])

    return ans


def get_near_less3(nums):
    N = len(nums)
    left = [-1] * N  # left[i] 为左侧严格小于等于 nums[i] 的最近元素位置（不存在时为-1）
    right = [-1] * N  # right[i] 为右侧严格小于 nums[i] 的最近元素位置（不存在时为 -1）
    st = []
    for i, n in enumerate(nums):
        while st and nums[st[-1]] > n:
            popi = st.pop()
            right[popi] = i
        left[i] = st[-1] if st else -1
        st.append(i)

    return [[l, r] for l, r in zip(left, right)]


def get_near_less_no_repeat2(arr):
    ans = [[]] * len(arr)
    stack = []

    for i, e in enumerate(arr):
        # 如果破坏了栈单调性
        while stack and arr[stack[-1]] > e:
            pop_index = stack.pop()
            left = stack[-1] if stack else -1
            ans[pop_index] = [left, i]

        stack.append(i)

    while stack:
        pop_index = stack.pop()
        left = stack[-1] if stack else -1
        ans[pop_index] = [left, -1]

    return ans


# 存在重复元素的单调栈
def get_near_less(arr):
    ans = [[]] * len(arr)
    stack = []

    for i, e in enumerate(arr):
        # 如果破坏了栈单调性
        while stack and arr[stack[-1][0]] > e:
            pop_indexs = stack.pop()
            # 取位于下面位置列表中，最晚加入的那个
            left = stack[-1][-1] if stack else -1
            for p_i in pop_indexs:
                ans[p_i] = [left, i]

        if stack and arr[stack[-1][0]] == e:
            stack[-1].append(i)
        else:
            stack.append([i])

    while stack:
        pop_indexs = stack.pop()
        # 取位于下面位置列表中，最晚加入的那个
        left = stack[-1][-1] if stack else -1
        for p_i in pop_indexs:
            ans[p_i] = [left, -1]

    return ans


import unittest


class TestMonotonicStack(unittest.TestCase):
    """ """

    def test_monotonic_stack1(self):
        self.assertEqual(
            [
                [-1, -1],
            ],
            get_near_less_no_repeat1([3]),
        )
        self.assertEqual(
            [
                [-1, 2],
                [0, 2],
                [-1, -1],
                [2, 5],
                [3, 5],
                [2, -1],
                [5, -1],
            ],
            get_near_less_no_repeat1([3, 4, 1, 5, 6, 2, 7]),
        )

    def test_monotonic_stack2(self):
        self.assertEqual(
            [
                [-1, -1],
            ],
            get_near_less_no_repeat2([3]),
        )
        self.assertEqual(
            [
                [-1, 2],
                [0, 2],
                [-1, -1],
                [2, 5],
                [3, 5],
                [2, -1],
                [5, -1],
            ],
            get_near_less_no_repeat2([3, 4, 1, 5, 6, 2, 7]),
        )

        print("aaa")
        self.assertEqual(
            [
                [-1, -1],
            ],
            get_near_less3([3]),
        )
        self.assertEqual(
            [
                [-1, 2],
                [0, 2],
                [-1, -1],
                [2, 5],
                [3, 5],
                [2, -1],
                [5, -1],
            ],
            get_near_less3([3, 4, 1, 5, 6, 2, 7]),
        )

    def test_monotonic_stack3(self):
        self.assertEqual(
            [
                [-1, -1],
            ],
            get_near_less_no_repeat2([3]),
        )
        self.assertEqual(
            [
                [-1, 2],
                [0, 2],
                [-1, -1],
                [2, 5],
                [3, 5],
                [2, -1],
                [5, -1],
            ],
            get_near_less([3, 4, 1, 5, 6, 2, 7]),
        )
        self.assertEqual(
            [
                [-1, 1],  # 0
                [-1, -1],  # 1
                [1, 7],  # 2
                [2, 4],  # 3
                [1, 7],  # 4
                [4, 6],  # 5
                [1, 7],  # 6
                [1, -1],  # 7
                [1, -1],  # 8
            ],
            get_near_less([3, 1, 3, 4, 3, 5, 3, 2, 2]),
        )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
