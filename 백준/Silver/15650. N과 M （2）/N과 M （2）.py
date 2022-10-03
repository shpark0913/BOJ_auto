N, M = map(int, input().split())

def nCr(n, r, s):
    if r == 0:
        print(*comb[::-1])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)
A = [i for i in range(1, N+1)]
comb = [0] * M
nCr(N, M, 0)