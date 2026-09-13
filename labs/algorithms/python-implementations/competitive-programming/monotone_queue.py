"""早期单调队列实现，保留用于与稳定软件包版本比较。

稳定、经过边界测试的实现是 ``algorithms.sliding_window_max``。本文件仍保留早期返回 ``None`` 和列表队头
删除的行为，便于学习时分析接口设计与复杂度差异，不应作为新代码依赖。
"""


def get_max_window(arr, w):
    if not arr or w < 1:
        return None

    ans = [-1] * (len(arr) - w + 1)
    qmax = []
    index = 0
    for i, element in enumerate(arr):
        while qmax and arr[qmax[-1]] <= element:
            qmax.pop()

        qmax.append(i)
        if qmax[0] == i - w:
            qmax.pop(0)
        if i >= w - 1:
            ans[index] = arr[qmax[0]]
            index += 1

    return ans
