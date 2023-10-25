def solution(arr):
    answer = []
    min_value = min(arr)
    for i in arr:
        if min_value != i:
            answer.append(i)
    if not answer:
        return [-1]
    return answer