import sys
input = sys.stdin.readline

T = int(input())
k = int(input())

coins = [list(map(int, input().split())) for _ in range(k)]
result = [0] * (T + 1)
result[0] = 1

for p, n in coins:
    for t in range(T, 0, -1):
        for s in range(1, n + 1):
            ans = t - (p * s)
            if ans >= 0:
                result[t] += result[ans]

print(result[T])