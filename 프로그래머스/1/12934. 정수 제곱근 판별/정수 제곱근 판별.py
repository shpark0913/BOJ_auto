def solution(n):
    answer = 0
    if int(n ** (1 / 2)) == n ** (1 / 2):
        return (int(n ** (1 / 2)) + 1) ** 2
    return -1