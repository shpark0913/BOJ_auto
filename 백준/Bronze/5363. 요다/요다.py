N = int(input())

lst = [list(input().split()) for _ in range(N)]


for l in lst:
    ans = []
    for i in range(2, len(l)):
        ans.append(l[i])
    for i in range(0, 2):
        ans.append(l[i])
    print(*ans)