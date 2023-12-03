# from itertools import product

# def solution(numbers, target):
#     ans = 0
#     data = [1, -1]
#     results = list(product(data, repeat=len(numbers)))
#     for result in results:
#         answer = 0
#         for i in range(len(result)):
#             answer += (result[i] * numbers[i])
#         if target == answer:
#             ans += 1
#     return ans

answer = 0

def dfs(index, numbers, target, value):
    global answer
    if index == len(numbers):
        if target == value:
            answer += 1
            return
        return
    dfs(index + 1, numbers, target, value + numbers[index])
    dfs(index + 1, numbers, target, value - numbers[index])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer