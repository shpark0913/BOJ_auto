def solution(n):
    lst = []
    for i in str(n):
        lst.append(i)
    lst.sort(reverse=True)
    answer = ""
    for l in lst:
        answer += str(l)
    return int(answer)