from collections import deque

def bfs(graph, x, y, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]  
    visited[x][y] = 1
    queue = deque([[x, y]])
    while queue:
        [x1, y1] = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x1][y1] + 1
                queue.append([nx, ny])

def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    bfs(maps, 0, 0, visited)
    answer = visited[-1][-1]
    if not answer: return -1
    return answer