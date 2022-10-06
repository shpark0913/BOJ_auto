from collections import deque
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if castle[nx][ny] == 2:
                    shortcut = path_time[x][y] + N - nx + M - 1 - ny
                    shortcut_lst.append(shortcut)
                elif visited[nx][ny] == 0 and castle[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    path_time[nx][ny] = path_time[x][y] + 1
N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
path_time = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
shortcut_lst = []
bfs(0, 0)
if shortcut_lst and path_time[N-1][M-1] == 0:
    if shortcut_lst[0] <= T:
        print(shortcut_lst[0])
    else:
        print('Fail')
elif shortcut_lst:
    if min(path_time[N - 1][M - 1], shortcut_lst[0]) <= T:
        print(min(path_time[N - 1][M - 1], shortcut_lst[0]))
    else:
        print('Fail')
elif 0 < path_time[N-1][M-1] <= T:
    print(path_time[N-1][M-1])
else:
    print('Fail')