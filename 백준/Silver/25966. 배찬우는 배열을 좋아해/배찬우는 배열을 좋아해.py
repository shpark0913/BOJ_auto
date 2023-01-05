import sys
input = sys.stdin.readline

N, M, q = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0]:
        arr[query[1]], arr[query[2]] = arr[query[2]], arr[query[1]]
    else:
        arr[query[1]][query[2]] = query[-1]

for elt in arr:
    print(*elt)