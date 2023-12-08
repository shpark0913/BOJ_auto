answer = 0

def dfs(numbers, target, index, value):
    global answer
    if index == len(numbers):
        if value == target:
            answer += 1
        return
    dfs(numbers, target, index + 1, value + numbers[index])
    dfs(numbers, target, index + 1, value - numbers[index])

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer