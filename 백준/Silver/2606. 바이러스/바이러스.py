from collections import deque

N = int(input())

E = int(input())

def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        visited[v] = 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt += 1

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
cnt = 0
bfs(1)
print(cnt)