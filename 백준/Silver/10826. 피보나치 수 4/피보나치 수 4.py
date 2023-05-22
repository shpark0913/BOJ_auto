import sys
input = sys.stdin.readline

n = int(input())

if not n:
    print(0)
    exit(0)

dp = [0] * (n + 1)

dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])