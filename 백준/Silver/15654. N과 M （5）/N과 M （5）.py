N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def f(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = 1
                p[i] = arr[j]
                f(i+1, k, r)
                used[j] = 0
used = [0] * len(arr)
p = [0] * M
f(0, len(arr), M)