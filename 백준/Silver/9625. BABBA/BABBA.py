K = int(input())

dp = [[] for _ in range(K + 1)]

dp[0] = [1, 0]

for i in range(1, K + 1):
    A, B = dp[i - 1][0], dp[i - 1][1]
    dp[i] = B, A + B

print(*dp[i])
