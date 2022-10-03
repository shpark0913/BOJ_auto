N, M = map(int, input().split())

def f(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k, r)
                used[j] = 0

a = [i for i in range(1, N+1)]
p = [0] * M
used = [0] * len(a)
f(0, len(a), M)
