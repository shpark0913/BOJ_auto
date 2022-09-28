N, M = map(int,input().split())

d = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    d[i][1] = 1
for j in range(1, M+1):
    d[1][j] = 1

for i in range(2, N+1):
    for j in range(2, M+1):
        d[i][j] = d[i-1][j] + d[i][j-1] + d[i-1][j-1]

print(d[N][M] % 1000000007)