N = int(input())
spots = {}

for _ in range(N):
    x, y = map(int, input().split())
    if x in spots.keys():
        spots[x].append(y)
    else:
        spots[x] = [y]

key_list = list(spots.keys())
key_list.sort()
for i in key_list:
    value_list = sorted(list(spots[i]))
    for j in value_list:
        print(i, j)