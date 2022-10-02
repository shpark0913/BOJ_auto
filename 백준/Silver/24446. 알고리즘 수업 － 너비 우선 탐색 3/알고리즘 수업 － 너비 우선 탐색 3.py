'''
9 7 1
1 2
1 3
2 4
2 5
3 6
3 7
4 8
'''
from collections import deque

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)

N, M, R = map(int, input().split())      # N : 정점의 수 / M : 간선의 수 / R : 시작 정점

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

BFS(R)
visited.pop(0)
for elt in visited:
    print(elt-1)