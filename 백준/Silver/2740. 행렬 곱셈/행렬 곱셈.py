N, M = map(int, input().split())

arrA = []
arrB = []

for _ in range(N):
    arrA.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    arrB.append(list(map(int, input().split())))

arrC = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            arrC[n][k] += arrA[n][m] * arrB[m][k]

for i in arrC:
    for j in i:
        print(j, end = ' ')
    print()