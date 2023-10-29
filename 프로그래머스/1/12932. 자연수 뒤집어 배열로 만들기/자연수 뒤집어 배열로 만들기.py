def solution(n):
    n = str(n)
    n = n[::-1]
    answer = []
    for i in n:
        answer.append(int(i))
    return answer