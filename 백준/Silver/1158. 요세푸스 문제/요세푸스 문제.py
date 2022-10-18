N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
arr2 = []
idx = K - 1

for i in range(N):
    if len(arr) > idx:
        arr2.append(arr.pop(idx))
        idx += (K-1)
    elif len(arr) <= idx:
        idx = idx % len(arr)
        arr2.append(arr.pop(idx))
        idx += (K-1)

print('<', end='')
for i in range(len(arr2)-1):
    print(f'{arr2[i]}, ', end='')
print(f'{arr2[-1]}>')