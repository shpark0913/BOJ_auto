def solution(a, b, n):
    answer = 0
    while 1:
        if n < a:
            break
        n -= (a - b)
        answer += b
    return answer