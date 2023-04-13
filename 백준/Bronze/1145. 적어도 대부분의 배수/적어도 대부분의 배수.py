lst = list(map(int, input().split()))
n = min(lst)
while 1:
    cnt = 0
    for i in range(5):
        if n % lst[i] == 0:
            cnt += 1
    if cnt > 2:
        print(n)
        break
    n += 1