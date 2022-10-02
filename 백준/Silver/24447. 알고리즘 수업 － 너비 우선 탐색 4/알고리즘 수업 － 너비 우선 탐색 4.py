from collections import deque

def BFS(v):
    global cnt
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.popleft()
        cnt += 1
        dic[v] = cnt
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
cnt = 0
dic = {}
for elt in graph:
    elt.sort()
BFS(R)
for i in range(len(visited)):
    visited[i] -= 1
s = 0
for i in range(1, N+1):
    if i in dic.keys():
        s += visited[i]*dic[i]
print(s)