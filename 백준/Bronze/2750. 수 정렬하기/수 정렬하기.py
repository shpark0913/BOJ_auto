N = int(input())

lst = [int(input()) for _ in range(N)]

lst.sort()

for l in lst:
    print(l)