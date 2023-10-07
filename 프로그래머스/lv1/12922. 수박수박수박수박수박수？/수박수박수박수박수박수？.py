def solution(n):
    Q, R = n // 2, n % 2
    answer = "수박" * Q
    if R:
        answer += "수"
    return answer