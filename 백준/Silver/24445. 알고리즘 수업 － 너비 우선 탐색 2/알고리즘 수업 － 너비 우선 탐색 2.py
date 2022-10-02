from collections import deque

def BFS(v):
    global cnt
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        visited[v] = 1
        cnt += 1
        dic[v] = cnt
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

N, M, R = map(int, input().split())      # N : 정점의 수 / M : 간선의 수 / R : 시작 정점

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
cnt = 0
dic = {}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for elt in graph:
    elt.sort(reverse=True)

BFS(R)

for i in range(1, N+1):
    if i in dic.keys():
        print(dic[i])
    else:
        print(0)