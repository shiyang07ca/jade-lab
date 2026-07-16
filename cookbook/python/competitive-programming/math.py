# 埃氏筛
# 素数筛
# https://zhuanlan.zhihu.com/p/100051075
MX = 10**5 + 1
omega = [0] * MX  # omega[i] 表示 i 的质因子种类数
for i in range(2, MX):  # 预处理 omega
    if omega[i] == 0:  # i 是质数
        for j in range(i, MX, i):
            omega[j] += 1  # i 是 j 的一个质因子


def eratosthenes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]


# TODO: 欧拉筛
"""
bool isnp[MAXN];
vector<int> primes; // 质数表
void init(int n)
{
    for (int i = 2; i <= n; i++)
    {
        if (!isnp[i])
            primes.push_back(i);
        for (int p : primes)
        {
            if (p * i > n)
                break;
            isnp[p * i] = 1;
            if (i % p == 0)
                break;
        }
    }

"""

if __name__ == "__main__":
    print(eratosthenes(120))
