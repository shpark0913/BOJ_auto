from itertools import product

def solution(numbers, target):
    ans = 0
    data = [1, -1]
    results = list(product(data, repeat=len(numbers)))
    for result in results:
        answer = 0
        for i in range(len(result)):
            answer += (result[i] * numbers[i])
        if target == answer:
            ans += 1
    return ans