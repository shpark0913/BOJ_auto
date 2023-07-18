num = int(input())
total = 0
cnt = 0

while 1:
    cnt += 1
    total += cnt
    if total > num:
        break

print(cnt-1)