from collections import deque

def bfs(graph, visited, v):
    visited[v] = True
    queue = deque([v])
    while queue:
        q = queue.popleft()
        for i in range(len(graph[q])):
            if not visited[i] and graph[q][i]:
                visited[i] = True
                queue.append(i)
        

def solution(n, computers):
    distance = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            distance += 1
            bfs(computers, visited, i)
    return distance