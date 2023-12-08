from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, visited, a, b, N, M):
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

def solution(maps):
    N, M = len(maps), len(maps[0])
    
    visited = [[False] * M for _ in range(N)]
    bfs(maps, visited, 0, 0, N, M)

    if visited[-1][-1]:
        return maps[-1][-1]
    else:
        return -1
