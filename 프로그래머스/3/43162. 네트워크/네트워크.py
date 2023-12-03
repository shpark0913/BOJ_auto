from collections import deque

def bfs(graph, visited, v, distance):
    print("#################")
    visited[v] = distance
    queue = deque([v])
    while queue:
        q = queue.popleft()
        print("q :", q)
        for i in range(len(graph[q])):
            if not visited[i] and graph[q][i]:
                visited[i] = distance
                queue.append(i)
        

def solution(n, computers):
    distance = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            distance += 1
            bfs(computers, visited, i, distance)
    answer = max(visited)
    return answer