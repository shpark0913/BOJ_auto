import sys
from collections import deque

input = sys.stdin.readline

# 사람의 수
n = int(input())

a, b = map(int, input().split())

relations = [[] for _ in range(101)]
visited = [0 for _ in range(101)]

# 부모, 자식 관계의 수
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

def bfs(V):
    queue = deque([V])
    while queue:
        q = queue.popleft()
        for i in relations[q]:
            if not visited[i]:
                visited[i] = visited[q] + 1
                queue.append(i)

bfs(a)

print(visited[b] if visited[b] else -1)