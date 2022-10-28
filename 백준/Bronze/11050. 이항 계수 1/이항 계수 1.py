N, K = map(int, input().split())

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

if N//2 < K:
    K = N - K

ZA = N
for i in range(1, K):
    ZA *= (N - i)

MO = fac(K)

if N == K or K == 0:
    print(1)
else:
    print(ZA // MO)