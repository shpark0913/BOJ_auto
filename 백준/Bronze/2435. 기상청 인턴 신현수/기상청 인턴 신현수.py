N, K = map(int, input().split())

temps = list(map(int, input().split()))

maxValue = -1000

for i in range(len(temps) - K + 1):
    isMax = 0
    for j in range(K):
        isMax += temps[i+j]
    if maxValue < isMax:
        maxValue = isMax

print(maxValue)