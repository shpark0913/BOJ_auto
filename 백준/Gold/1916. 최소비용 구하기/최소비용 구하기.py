import heapq
import sys
input = sys.stdin.readline

# 도시의 개수
N = int(input())

# 버스의 개수
M = int(input())

graph = [[] for _ in range(N + 1)]

distance = [int(1e9)] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

dijkstra(start)

print(distance[end])
