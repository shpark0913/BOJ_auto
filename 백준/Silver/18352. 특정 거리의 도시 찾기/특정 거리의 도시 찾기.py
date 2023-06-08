import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(X)

if K in distance:
    for i in range(len(distance)):
        if distance[i] == K:
            print(i)
else:
    print(-1)