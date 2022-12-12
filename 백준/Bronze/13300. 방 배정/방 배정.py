N, K = map(int, input().split())

boys = {}
girls = {}
roomNums = 0
for _ in range(N):
    S, Y = map(int, input().split())
    if S:
        if Y in boys.keys(): boys[Y] += 1
        else: boys[Y] = 1
    else:
        if Y in girls.keys(): girls[Y] += 1
        else: girls[Y] = 1

if boys.values():
    for elt in boys.values():
        if elt > K:
            if elt%K:
                roomNums += (elt//K + 1)
            else:
                roomNums += elt//K
        else:
            roomNums += 1
if girls.values():
    for elt in girls.values():
        if elt > K:
            if elt%K:
                roomNums += (elt//K + 1)
            else:
                roomNums += elt//K
        else:
            roomNums += 1
print(roomNums)