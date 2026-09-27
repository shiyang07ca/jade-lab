"""二分查找：只记一套「在 [left, right) 找第一个真」的模板。

记忆规则
========
条件随位置增大必须呈「假 ... 假 真 ... 真」，允许全假或全真。
中点为真：right = middle（中点可能是答案，继续向左找）。
中点为假：left = middle + 1（中点及左侧都不可能是答案）。
循环结束：left == right，返回分界点；无解返回原来的 right。

数组查找
========
values 必须升序（允许重复），元素与 target 的比较须有一致的大小关系；
不自动排序或检查单调性。不适用于含 NaN 等破坏比较关系的输入。
设 n = len(values)，L = lower_bound(values, x)，U = upper_bound(values, x)：

    需求                  结果                 使用前的检查
    第一个 >= x           L                    L < n
    第一个 > x            U                    U < n
    最后一个 < x          L - 1                L > 0
    最后一个 <= x         U - 1                U > 0
    等于 x 的下标区间     [L, U)               L == U 表示不存在
    等于 x 的数量         U - L                无需额外检查
    第一个 == x           binary_search(a, x)  用 is not None 判断

n 和 -1 都可能表示不存在，不能直接索引；Python 的 a[-1] 会取末尾元素。
对于 a = [1, 3, 3, 3, 8]：

    x     lower_bound    upper_bound    binary_search
    0          0              0              None
    1          0              1                 0
    3          1              4                 1
    4          4              4              None
    8          4              5                 4
    9          5              5              None
    空数组对任意 x 都返回：0、0、None。

二分答案（不需要数组）
====================
在整数闭区间 [lo, hi] 中搜索时，传入 first_true(lo, hi + 1, check)。
求最小可行值：check 须先假后真；返回 hi + 1 表示无解。
求最大可行值：ok 须先真后假，找第一个不可行值再减一：
first_true(lo, hi + 1, lambda x: not ok(x)) - 1。
此时返回 lo - 1 表示无解，全可行则返回 hi；哨兵不需要实际满足条件。

>>> first_true(0, 21, lambda k: k * k >= 20)  # 最小 k，使 k² >= 20
5
>>> first_true(0, 91, lambda k: k * k > 90) - 1  # 最大 k，使 k² <= 90
9
>>> lower_bound([1, 3, 3, 3, 8], 3), upper_bound([1, 3, 3, 3, 8], 3)
(1, 4)
>>> binary_search([1, 3, 3, 3, 8], 1)  # 下标 0 也表示找到了
0

普通 list 查找耗时 O(log n)，额外空间 O(1)；通用模板的耗时还要乘上
predicate 单次判断的成本。

标准库 bisect
=============
bisect_left / bisect_right 返回插入位置，不修改数组：

    标准库                 本文件          含义
    bisect_left(a, x)       lower_bound     第一个 >= x
    bisect_right(a, x)      upper_bound     第一个 > x

记忆：left 在相等元素左侧，right 在相等元素右侧。
返回位置不代表目标存在；精确查找仍需检查下标和元素是否相等。

>>> from bisect import bisect_left, bisect_right
>>> a = [1, 3, 3, 3, 8]
>>> bisect_left(a, 3), bisect_right(a, 3)
(1, 4)
>>> bisect_left(a, 4), bisect_right(a, 4)
(4, 4)

可选参数 lo、hi 限定搜索区间 [lo, hi)，返回原数组的下标；
空区间返回 lo，找不到满足条件的位置时返回 hi。
"""

from collections.abc import Callable


def first_true(left: int, right: int, predicate: Callable[[int], bool]) -> int:
    """在整数区间 [left, right) 找第一个真；无解返回原 right。

    前提：left <= right，predicate 单调地由假变真，且搜索期间结果不变。
    空区间直接返回 right，不调用 predicate；永远不判断原 right。
    单调性由调用方保证。传入反向区间时抛出 ValueError。
    """
    if left > right:
        raise ValueError("left must not exceed right")
    while left < right:
        middle = (left + right) // 2
        # 不变量：原搜索范围内，left 左侧全假，right 及其右侧全真。
        # [left, right) 是待确定区间，最终答案仍可以等于 right。
        if predicate(middle):
            right = middle
        else:
            left = middle + 1
    return left


def lower_bound(values, target) -> int:
    """在升序序列中找第一个 >= target 的下标；无解返回 len(values)。"""
    return first_true(0, len(values), lambda i: values[i] >= target)


def upper_bound(values, target) -> int:
    """在升序序列中找第一个 > target 的下标；无解返回 len(values)。"""
    return first_true(0, len(values), lambda i: values[i] > target)


def binary_search(values, target) -> int | None:
    """返回 ``target`` 首次出现的下标；若不存在则返回 ``None``。"""
    index = lower_bound(values, target)
    return index if index < len(values) and values[index] == target else None
