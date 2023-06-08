import heapq
import sys
input = sys.stdin.readline

# 도시의 개수
nums_city = int(input())

# 버스의 개수
nums_bus = int(input())

# 노선의 정보
graph = [[] for _ in range(nums_city + 1)]

distance = [int(1e9)] * (nums_city + 1)

for _ in range(nums_bus):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, arrive = map(int, input().split())

def dijkstra(s):
    distance[s] = 0
    q = []
    heapq.heappush(q, [0, s])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, [distance[i[0]], i[0]])


dijkstra(start)

if distance[arrive] == int(1e9):
    print(-1)
else:
    print(distance[arrive])