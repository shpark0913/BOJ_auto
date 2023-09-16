N = int(input())

dp = [0, 1, 1, 2, 3]

if N <= 4:
    print(dp[N])
else:
    for i in range(5, N + 1):
        dp.append(dp[i - 2] + dp[i - 1])
    print(dp[N])