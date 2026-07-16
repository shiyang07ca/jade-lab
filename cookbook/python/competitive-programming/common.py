# 二维前缀和


# 二维前缀和模板
# LC1444/周赛188D https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/
class MatrixSum:
    def __init__(self, matrix: List[str]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    # 返回左上角在 (r1,c1) 右下角在 (r2-1,c2-1) 的子矩阵元素和（类似前缀和的左闭右开）
    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2][c2] - self.s[r2][c1] - self.s[r1][c2] + self.s[r1][c1]


# 差分数组
# 你有一个长为 n 的数组 a，一开始所有元素均为 0。
# 给定一些区间操作，其中 queries[i] = [left, right, x]，
# 你需要把子数组 a[left], a[left+1], ... a[right] 都加上 x。
# 返回所有操作执行完后的数组 a。
def solve(n: int, queries: List[List[int]]) -> List[int]:
    diff = [0] * n  # 差分数组
    for left, right, x in queries:
        diff[left] += x
        if right + 1 < n:
            diff[right + 1] -= x
    for i in range(1, n):
        diff[i] += diff[i - 1]  # 直接在差分数组上复原数组 a
    return diff


"""
例题

LC1094. 拼车 https://leetcode.cn/problems/car-pooling/description/
LC1109. 航班预订统计 https://leetcode.cn/problems/corporate-flight-bookings/description/
LC2381. 字母移位 II https://leetcode.cn/problems/shifting-letters-ii/description/
LC2406. 将区间分为最少组数 https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/description/
LC2772. 使数组中的所有元素都等于零 https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/description/
LC2528. 最大化城市的最小供电站数目 https://leetcode.cn/problems/maximize-the-minimum-powered-city/description/
"""
