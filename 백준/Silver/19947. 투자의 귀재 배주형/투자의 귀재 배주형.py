import math

dp = [0] * 11

# H : 초기 비용, Y : 투자 기간
H, Y = map(int, input().split())

dp[0] = H

for i in range(1, Y + 1):
    if i in [1, 2]:
        dp[i] = dp[i - 1] * 1.05
    elif i in [3, 4]:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2)
    else:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2, dp[i - 5] * 1.35)
    dp[i] = int(dp[i])

print(math.trunc(dp[Y]))
