from collections import deque
import sys

def BFS():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i, j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
all_tomatoes = []
BFS()
for elt in tomatoes:
    all_tomatoes += elt
if 0 in all_tomatoes:
    print(-1)
else:
    print(max(all_tomatoes) - 1)