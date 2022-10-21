n = list(input())
cnt = 0

if len(n) == 1:
    print(0)
    if int(n[-1]) in {3, 6, 9}:
        print("YES")
    else:
        print("NO")
else:
    while 1:
        s = 0
        for elt in n:
            s += int(elt)
        cnt += 1
        if s < 10:
            print(cnt)
            if s in {3, 6, 9}:
                print('YES')
                break
            else:
                print('NO')
                break
        else:
            n = list(str(s))

