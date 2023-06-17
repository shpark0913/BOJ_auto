N = int(input())

classroom = []

for _ in range(N):
    line = list(map(int, input().split()))
    classroom.append(line)

spots = []

for i in range(N):
    if len(spots) == 2: break
    for j in range(N):
        if len(spots) == 2: break
        if classroom[i][j] in [2, 5]:
            spots.append([i, j])

x1, x2, y1, y2 = min(spots[0][0], spots[1][0]), max(spots[0][0], spots[1][0]), min(spots[0][1], spots[1][1]), max(spots[0][1], spots[1][1])

cnt = 0

def can_run(spots):
    l = ((spots[0][0] - spots[1][0]) ** 2 + (spots[0][1] - spots[1][1]) ** 2) ** (1 / 2)
    if l >= 5:
        return True
    else:
        return False

for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
        if classroom[x][y] == 1:
            cnt += 1

if can_run(spots) and cnt >= 3:
    print(1)
else:
    print(0)
