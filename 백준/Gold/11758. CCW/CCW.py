[x1, y1] = list(map(int, input().split()))
[x2, y2] = list(map(int, input().split()))
[x3, y3] = list(map(int, input().split()))


# (a, b), (c, d) 두 점을 지나는 직선의 방정식에
# 특정 x값을 넣었을 때 나오는 y값
def y_spot(a, b, c, d, x):
    ans = ((d - b)/(c - a)) * (x - a) + b
    return ans


# 세 점이 일직선인 경우
if x1 == x2 == x3 or y1 == y2 == y3 or (x1 != x2 and x1 != x3 and (y2-y1)/(x2-x1) == (y3-y1)/(x3-x1)) or (x3 != x2 and x1 != x3 and (y2-y3)/(x2-x3) == (y3-y1)/(x3-x1)) or (x2 != x1 and x2 != x3 and (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)):
    print(0)
    exit(0)

# 세 점 중 2개의 점의 x좌표가 같은 경우
if x1 == x2:
    if y1 < y2:
        if x3 > x1:
            print(-1)
            exit(0)
        else:
            print(1)
            exit(0)
    else:
        if x3 > x1:
            print(1)
            exit(0)
        else:
            print(-1)
            exit(0)
elif x1 == x3:
    if y1 < y3:
        if x2 > x1:
            print(1)
            exit(0)
        else:
            print(-1)
            exit(0)
    else:
        if x2 > x1:
            print(-1)
            exit(0)
        else:
            print(1)
            exit(0)
elif x2 == x3:
    if y2 < y3:
        if x2 > x1:
            print(1)
            exit(0)
        else:
            print(-1)
            exit(0)
    else:
        if x2 > x1:
            print(-1)
            exit(0)
        else:
            print(1)
            exit(0)

# 세 점의 x좌표가 모두 다른 경우
if x1 < x2:
    if y3 < y_spot(x1, y1, x2, y2, x3):
        print(-1)
        exit(0)
    else:
        print(1)
        exit(0)

elif x1 > x2:
    if y3 < y_spot(x1, y1, x2, y2, x3):
        print(1)
        exit(0)
    else:
        print(-1)
        exit(0)