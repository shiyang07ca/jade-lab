import math

# 筛质数

# 埃氏筛
def get_primes():
    MX = 10**6 + 1
    primes = []
    is_prime = [True] * MX
    for i in range(2, MX):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, MX, i):
                is_prime[j] = False
    primes.extend((MX, MX))  # 保证下面下标不会越界


# 线性筛(欧拉筛)
def get_primes():
    MX = 10**6 + 1
    primes = []
    is_prime = [True] * MX
    for i in range(2, MX):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p >= MX:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break
    primes.extend((MX, MX))  # 保证下面下标不会越界


# 分解质因数
def get_prime_factor(num):
    # 质因数分解
    res = []
    for i in range(2, int(math.sqrt(num)) + 1):
        cnt = 0
        while num % i == 0:
            num //= i
            cnt += 1
        if cnt:
            res.append([i, cnt])
        if i > num:
            break
    if num != 1 or not res:
        res.append([num, 1])
    # 从小到大返回质因数分解以及对应的幂次，注意 1 返回 []
    return res


def get_prime_factor2(num):
    res = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            res.append(i)
            num //= i
            while num % i == 0:
                num //= i
        i += 1
    if num > 1:
        res.append(num)

    return res


if __name__ == "__main__":
    nums = list(range(20))
    for n in nums:
        print(n, get_prime_factor(n), get_prime_factor2(n))
