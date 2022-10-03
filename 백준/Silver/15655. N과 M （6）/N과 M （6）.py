N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def nCr(n, r, s):
    if r == 0:
        print(*comb[::-1])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = arr[i]
            nCr(n, r-1, i+1)
comb = [0] * M
nCr(N, M, 0)