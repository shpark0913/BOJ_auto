from collections import deque
def BFS(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited[node] = True
        for childNode in treeDict[node]:
            if not visited[childNode]:
                ans[childNode] = node
                queue.append(childNode)


V = int(input())
treeDict = {}
for i in range(1, V+1):
    treeDict[i] = []
for _ in range(V-1):
    a, b = map(int, input().split())
    treeDict[a].append(b)
    treeDict[b].append(a)

visited = [False] * (V+1)
ans = [0] * (V+1)
BFS(1)
print('\n'.join(map(str, ans[2:])))