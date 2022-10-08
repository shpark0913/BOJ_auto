N, M = map(int, input().split())

arr = list(input() for _ in range(N))

for elt in arr:
    print(elt[::-1])