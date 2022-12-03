arr = [input() for _ in range(8)]
cnt = 0
for i in range(len(arr)):
    if i%2:
        for j in range(8):
            if j%2 and arr[i][j] == 'F':
                cnt += 1
    else:
        for j in range(8):
            if (not j%2) and arr[i][j] == 'F':
                cnt += 1
print(cnt)