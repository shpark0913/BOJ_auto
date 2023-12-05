from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, a, b):
    q = deque([(a, b)])
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    bfs(maps, visited, 0, 0)
    
    answer = visited[len(maps) - 1][len(maps[0]) - 1]
    if answer:
        return answer
    else:
        return -1