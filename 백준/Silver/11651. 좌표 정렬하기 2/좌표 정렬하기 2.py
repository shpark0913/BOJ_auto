N = int(input())
spots = {}

for _ in range(N):
    x, y = map(int, input().split())
    if y in spots.keys():
        spots[y].append(x)
    else:
        spots[y] = [x]

key_list = sorted(list(spots.keys()))
for j in key_list:
    value_list = sorted(list(spots[j]))
    for i in value_list:
        print(i, j)