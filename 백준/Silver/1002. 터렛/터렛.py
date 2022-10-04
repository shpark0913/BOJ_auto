T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = ((abs(x1-x2)**2)+(abs(y1-y2)**2))**(1/2)
    if x1 != x2 or y1 != y2:
        if r1 + r2 < distance or r2 > r1 + distance or r1 > r2 + distance:
            print(0)
        elif r1 + r2 == distance or distance == r2 - r1 or distance == r1 - r2:
            print(1)
        elif r1 + r2 > distance:
            print(2)

    else:
        if r1 == r2:
            if r1 == 0:
                print(1)
            else:
                print(-1)
        else:
            print(0)