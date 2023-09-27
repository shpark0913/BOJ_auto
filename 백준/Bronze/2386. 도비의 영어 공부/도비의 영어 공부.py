while 1:
    s = input()
    if s == "#":
        break
    a = s[0]
    b = s[2:]
    cnt = 0
    for i in b:
        if a in [i, i.lower()]:
            cnt += 1

    print(a, cnt)