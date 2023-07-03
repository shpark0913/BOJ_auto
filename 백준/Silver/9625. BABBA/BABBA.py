K = int(input())

dp = [1, 0]

for i in range(1, K + 1):
    A, B = dp[0], dp[1]
    dp = [B, A + B]

print(*dp)
