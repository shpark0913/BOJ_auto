import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if d == 0:
        if r1 == r2:
            if r1 == 0 and r2 == 0:
                print(1)
                continue
            print(-1)
            continue
        else:
            print(0)
            continue
    elif (r1 + r2) ** 2 > d:
        if max(r1, r2) == math.sqrt(d) + min(r1, r2):
            print(1)
            continue
        elif max(r1, r2) > math.sqrt(d) + min(r1, r2):
            print(0)
            continue
        print(2)
        continue
    elif (r1 + r2) ** 2 == d:
        print(1)
        continue
    else:
        print(0)
        continue