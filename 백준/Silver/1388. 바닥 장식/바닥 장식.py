import sys
input = sys.stdin.readline
N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
boardNum = 0
def dfs(floor, visited, i, j):
    global boardNum
    visited[i][j] = True
    boardNum += 1
    if floor[i][j] == '-':
        while 1:
            if j + 1 < M and floor[i][j+1] == '-':
                visited[i][j+1] = True
                j += 1
            else:
                break
    else:
        while 1:
            if i + 1 < N and floor[i+1][j] == '|':
                visited[i+1][j] = True
                i += 1
            else:
                break
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            dfs(floor, visited, i, j)
print(boardNum)