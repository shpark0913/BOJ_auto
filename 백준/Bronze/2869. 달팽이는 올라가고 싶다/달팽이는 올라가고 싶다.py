A, B, V = map(int, input().split())

day = 0

ans = (V-B)/(A-B)

if ans == int(ans):
    print(int(ans))
else:
    print(int(ans) + 1)