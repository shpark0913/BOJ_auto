import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(a, b, maps, distance):
    q = []
    distance[a][b] = 1
    heapq.heappush(q, (1, (a, b)))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in range(4):
            nx, ny = now[0] + dx[i], now[1] + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                cost = dist + 1
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))

def solution(maps):
    INF = int(1e9)
    distance = [[INF] * len(maps[0]) for _ in range(len(maps))]
    dijkstra(0, 0, maps, distance)
    answer = distance[-1][-1]
    if answer != INF:
        return answer
    else:
        return -1