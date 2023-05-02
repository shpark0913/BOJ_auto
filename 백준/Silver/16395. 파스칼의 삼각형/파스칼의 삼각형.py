from itertools import combinations

# 파스칼 삼각형의 N번째 줄의 k번째 수를 구하겠다.
N, K = map(int, input().split())

n = []

for i in range(1, N):
    n.append(i)

cnt = 0

for i in combinations(n, K-1):
    cnt += 1

print(cnt)