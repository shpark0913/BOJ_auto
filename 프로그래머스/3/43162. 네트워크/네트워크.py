from collections import deque

def bfs(graph, visited, v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    # n: 컴퓨터의 개수 / computers: 연결에 대한 정보
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(graph, visited, i)
    
    return answer