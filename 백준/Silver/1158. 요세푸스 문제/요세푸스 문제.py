N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
arr2 = []
idx = K - 1

for i in range(N):
    idx = idx % len(arr)
    arr2.append(arr.pop(idx))
    idx += (K-1)

print(f'<{str(arr2)[1:-1]}>')