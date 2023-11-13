def solution(left, right):
    answer = 0
    def getDivisor(n):
        divisorsList = []
        for i in range(1, n + 1):
            if (n % i == 0) :
                divisorsList.append(i)
        return int(len(divisorsList))
    for i in range(left, right + 1):
        num = getDivisor(i)
        if not num % 2:
            answer += i
        else:
            answer -= i
    return answer