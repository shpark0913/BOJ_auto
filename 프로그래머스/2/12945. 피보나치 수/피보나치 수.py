def solution(n):
    answer = 0
    dp = [0, 1, 1]
    if n < 3:
        answer = dp[n]
    else:
        for i in range(3, n + 1):
            dp.append(dp[i - 2] + dp[i - 1])
        answer = dp[n]
    return answer % 1234567