N, M = map(int, input().split())

def f(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = a[j]
            f(i+1, k, r)

a = [i for i in range(1, N+1)]
p = [0] * M
used = [0] * len(a)
f(0, len(a), M)