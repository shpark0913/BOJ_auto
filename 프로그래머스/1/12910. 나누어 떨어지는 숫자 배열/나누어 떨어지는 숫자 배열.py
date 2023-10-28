def solution(arr, divisor):
    answer = []
    for a in arr:
        if not a % divisor:
            answer.append(a)
    if not answer:
        return [-1]
    answer.sort()
    return answer