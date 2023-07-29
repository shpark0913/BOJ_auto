dp = [1, 1, 2, 3]

for _ in range(TC := int(input())):
    n = int(input())
    if n < len(dp):
        print(dp[n])
    elif n == len(dp):
        dp.append(dp[n - 1] + dp[n - 2])
        print(dp[n])
    else:
        for i in range(len(dp), n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        print(dp[n])
