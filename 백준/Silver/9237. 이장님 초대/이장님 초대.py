import sys
input = sys.stdin.readline

# 묘목의 개수
N = int(input())

# 묘목들의 높이
trees = sorted(list(map(int, input().split())), reverse=True)

for i in range(N):
    trees[i] += i
print(max(trees) + 2)