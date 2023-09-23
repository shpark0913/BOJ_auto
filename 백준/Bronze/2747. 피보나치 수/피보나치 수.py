N = int(input())

dp = [0, 1, 1, 2, 3, 5]

if N <= 5:
    print(dp[N])
else:
    for i in range(6, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    print(dp[N])