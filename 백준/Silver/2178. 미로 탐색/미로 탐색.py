from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
arr = [[0] * M for _ in range(N)]

visited = [[0] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])