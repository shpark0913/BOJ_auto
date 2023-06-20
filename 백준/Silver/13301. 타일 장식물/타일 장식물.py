N = int(input())

dp = [0] * 81

dp[1] = dp[2] = 1
dp[3] = 2
dp[4] = 3
dp[5] = 5

if N <= 5:
    print(4 * dp[N] + 2 * dp[N - 1])
else:
    for i in range(6, N + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(4 * dp[N] + 2 * dp[N - 1])
