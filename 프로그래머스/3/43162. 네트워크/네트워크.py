from collections import deque

def bfs(computers, visited, v):
    visited[v] = True
    queue = deque([v])
    while queue:
        q = queue.popleft()
        for i in range(len(computers[q])):
            if computers[q][i] == 1 and not visited[i]:
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