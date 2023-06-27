import sys
from collections import deque

N = int(input())

graph = [list(input().rstrip()) for _ in range(N)]

visited_normal = [[False] * N for _ in range(N)]
visited_abnormal = [[False] * N for _ in range(N)]

cnt_normal = 0
cnt_abnormal = 0

def bfs_normal(x, y):
    queue = deque([(x, y)])
    visited_normal[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited_normal[nx][ny] and graph[nx][ny] == graph[x][y]:
                queue.append((nx, ny))
                visited_normal[nx][ny] = True

def bfs_abnormal(x, y):
    queue = deque([(x, y)])
    visited_abnormal[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited_abnormal[nx][ny]:
                if graph[x][y] == 'B' and graph[nx][ny] == 'B':
                    queue.append((nx, ny))
                    visited_abnormal[nx][ny] = True
                elif graph[x][y] != 'B' and graph[nx][ny] != 'B':
                    queue.append((nx, ny))
                    visited_abnormal[nx][ny] = True

for a in range(N):
    for b in range(N):
        if not visited_normal[a][b]:
            bfs_normal(a, b)
            cnt_normal += 1
        if not visited_abnormal[a][b]:
            bfs_abnormal(a, b)
            cnt_abnormal += 1

print(cnt_normal, cnt_abnormal)
