import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 100001

for _ in range(N):
    n = int(input())
    dp[n] += 1
    
for i in range(len(dp)):
    if dp[i]:
        for _ in range(dp[i]):
            print(i)