N, M = map(int, input().split())

graph = []

dp = [1] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph.append((a, b))

graph.sort()

for before, after in graph:
    if dp[after] <= dp[before]:
        dp[after] = dp[before] + 1

print(*dp[1:])