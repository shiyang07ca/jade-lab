"""
"""
"""
"""


"""

单调队列 Monotone Queue

需要不断维护队列的单调性，时刻保证队列元素从大到小或从小到大
前置知识：双指针
以固定窗口大小的区间最大值为例（此时维护的是一个从大到小的单调队列）：
每次向右移动一格左指针，在移动前，如果左指针指向的元素在队首左侧，说明左指针指向的元素小于队首，移动左指针不会改变区间最大值，直接移动左指针即可；
如果左指针指向的就是队首，那么移动左指针会使区间最大值变小（变为单调队列队首之后的那个元素），我们要弹出队首。
这样无论是何种情况，都保证了在移动左指针后，单调队列的队首始终为当前区间的最大值。
https://oi-wiki.org/ds/monotonous-queue/
https://oi-wiki.org/dp/opt/monotonous-queue-stack/
https://cp-algorithms.com/data_structures/stack_queue_modification.html
https://blog.csdn.net/weixin_43914593/article/details/105791217 算法竞赛专题解析（13）：DP优化(3)--单调队列优化

模板题
LC239. 滑动窗口最大值 https://leetcode.cn/problems/sliding-window-maximum/


"""


"""
应用


生成窗口最大值数组

有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。

例如，数组为[4，3，5，4，3，3，6，7]，窗口大小为3时


[4, 3, 5], 4, 3, 3, 6, 7   5

4, [3, 5, 4], 3, 3, 6, 7   5

4, 3, [5, 4, 3], 3, 6, 7   5

4, 3, 5, [4, 3, 3], 6, 7   4

4, 3, 5, 4, [3, 3, 6], 7   6

4, 3, 5, 4, 3, [3, 6, 7]   7

输入：整型数组arr，窗口大小为w。

输出：一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值。以本题为例，结果应该返回{5，5，5，4，6，7}。
"""


def get_max_window(arr, w):
    if not arr or w < 1:
        return None

    ans = [-1] * (len(arr) - w + 1)
    qmax = []
    index = 0
    for i, e in enumerate(arr):
        while qmax and arr[qmax[-1]] <= e:
            qmax.pop()

        qmax.append(i)

        # 如果qmax队头的下标等于i-w，说明当前qmax队头的下标已过期,
        # 弹出当前队头的下标即可
        if qmax[0] == i - w:
            qmax.pop(0)

        # 窗口已经出现，开始计算最大值
        if i >= w - 1:
            ans[index] = arr[qmax[0]]
            index += 1

    return ans


import unittest


class Test(unittest.TestCase):
    def test_get_max_window(self):
        print("aaa")
        self.assertEqual(
            [5, 5, 5, 4, 6, 7], get_max_window([4, 3, 5, 4, 3, 3, 6, 7], 3)
        )


if __name__ == "__main__":
    unittest.main()
