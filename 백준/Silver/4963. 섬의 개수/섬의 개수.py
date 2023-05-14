from collections import deque

def bfs(graph, a, b):
    graph[a][b] = 0
    queue = deque([[a, b]])
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while queue:
        q = queue.popleft()
        for k in range(8):
            nx = q[0] + dx[k]
            ny = q[1] + dy[k]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append(([nx, ny]))


while 1:
    # 지도의 너비와 높이
    w, h = map(int, input().split())
    if [w, h] == [0, 0]: break

    # 지도를 나타 내는 이중 리스트
    maps = []

    # 섬의 개수
    islands = 0

    for _ in range(h):
        maps.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(maps, i, j)
                islands += 1

    print(islands)

