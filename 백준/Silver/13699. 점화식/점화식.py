n = int(input())

dp = [0] * 36

dp[0] = 1

for i in range(1, n + 1):
    ans = 0
    for j in range(i):
        ans += (dp[j] * dp[i - 1 - j])

    dp[i] = ans

print(dp[n])