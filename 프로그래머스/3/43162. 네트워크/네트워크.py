from collections import deque

def bfs(graph, visited, v):
    visited[v] = True
    queue = deque([v])
    while queue:
        q = queue.popleft()
        for i in range(len(graph[q])):
            if not visited[i] and graph[q][i] == 1:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(computers, visited, i)
    return answer