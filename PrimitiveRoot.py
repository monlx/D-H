import numpy as np
def judgeCoPrime(a, b):
    def maxCommonFactor(m, n):
        while m % n > 0:
            m, n = n, m % n
        return n
    return maxCommonFactor(a, b) == 1
def getPrimitiveRoot(primeNumber):
    primitiveRootList = []
    for i in range(1, primeNumber):
        if judgeCoPrime(i, primeNumber):
            tmpList = {(i ** j) % primeNumber for j in range(1, primeNumber)}
            if len(tmpList) == (primeNumber - 1):
                primitiveRootList.append(i)
    print(f"{primeNumber}的所有原根：\n", primitiveRootList)
    return primitiveRootList
def verify(p, g):
    seen = set()
    for i in range(1, g):
        result = (p ** i) % g
        print(f"{p}^{i} mod {g} = {result}")
        if result in seen:
            print("不是原根组!")
            return
        else:
            seen.add(result)
    print("是原根组！")
    return
if __name__ == '__main__':
    p = int(input("请输入质数p:"))
    getPrimitiveRoot(p)
    g = int(input(f"请输入{p}的原根g:"))
    verify(g, p)

