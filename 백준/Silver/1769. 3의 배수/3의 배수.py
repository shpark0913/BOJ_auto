n = list(input())
cnt = 0

if len(n) == 1:
    print(0)
    print('YES') if not int(n[-1]) % 3 else print('NO')
else:
    while 1:
        s = 0
        for elt in n:
            s += int(elt)
        cnt += 1
        if s < 10:
            print(cnt)
            print('NO') if s % 3 else print('YES')
            break
        else:
            n = list(str(s))

