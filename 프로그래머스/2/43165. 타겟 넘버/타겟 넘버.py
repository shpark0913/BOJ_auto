answer = 0

def dfs(graph, index, value, target):
    global answer
    if index == len(graph):
        if value == target:
            answer += 1
        return
    dfs(graph, index + 1, value + graph[index], target)
    dfs(graph, index + 1, value - graph[index], target)
        

def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer