T = int(input())

for _ in range(T):
    N = int(input())
    if N >= 10:
        dp = [1] * (N + 1)
    else:
        dp = [1] * 11
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    dp[8] = 5
    dp[9] = 7
    dp[10] = 9
    if N <= 10:
        print(dp[N])
    else:
        for i in range(11, N + 1):
            dp[i] = dp[i - 2] + dp[i - 3]
        print(dp[N])
