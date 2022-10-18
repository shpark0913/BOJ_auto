import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = 1
for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    for j in range(i-1):
        if k[j] < k[j+1]:
            p = 0
            break
    if not p: 
        break

print('Yes' if p else 'No') 