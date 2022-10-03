N, M = map(int, input().split())

def nHr(n, r, s):
    if r == 0:
        print(*comb[::-1])
    else:
        for i in range(s, n):
            comb[r-1] = A[i]
            nHr(n, r-1, i)

A = [i for i in range(1, N+1)]
comb = [0] * M
nHr(N, M, 0)
