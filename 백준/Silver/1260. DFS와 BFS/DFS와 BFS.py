import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

dfs_result = []
bfs_result = []


def dfs(graph, v, visited):
    visited[v] = True
    dfs_result.append(v)
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        q = queue.popleft()
        bfs_result.append(q)
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(graph, V, visited_dfs)
bfs(graph, V, visited_bfs)
print(*dfs_result)
print(*bfs_result)

