import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    dp = [1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if N <= 10:
        print(dp[N])
    else:
        for i in range(11, N + 1):
            dp.append(dp[i - 2] + dp[i - 3])
        print(dp[N])
