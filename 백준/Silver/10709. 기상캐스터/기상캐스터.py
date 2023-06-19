H, W = map(int, input().split())

areas = []

clouds = [[-1] * W for _ in range(H)]

for _ in range(H):
    area = list(input())
    areas.append(area)

# clouds_spot = [[] for _ in range(H)]
#
for i in range(H):
    for j in range(W):
        if areas[i][j] == 'c':
            clouds[i][j] = 0

for i in range(H):
    for j in range(W):
        if clouds[i][j] == -1:
            for k in range(j - 1, -1, -1):
                if areas[i][k] == "c":
                    clouds[i][j] = (j - k)
                    break

for cloud in clouds:
    print(*cloud)
