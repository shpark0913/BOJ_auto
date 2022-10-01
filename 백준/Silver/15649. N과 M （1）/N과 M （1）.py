N, M = map(int, input().split())

def f(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            if not visited[j]:
                visited[j] = 1
                p[i] = a[j]
                f(i+1, k, r)
                visited[j] = 0

a = [i for i in range(1, N+1)]

visited = [0] * N

p = [0] * M

f(0, N, M)