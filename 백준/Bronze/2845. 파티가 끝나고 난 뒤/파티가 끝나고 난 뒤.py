L, P = map(int, input().split())

lst = list(map(int, input().split()))
arr = []
for elt in lst:
    arr.append(-L*P + elt)
print(*arr)