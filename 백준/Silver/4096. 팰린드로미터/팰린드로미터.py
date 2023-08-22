while 1:
    N = input()
    c = 0
    if N == "0":
        exit(0)
    while N != N[::-1]:
        c += 1
        M = str(int(N) + 1)
        if len(N) != len(str(int(N))):
            if len(str(int(N))) == len(M):
                N = "0" * (len(N) - len(str(int(N)))) + M
            else:
                N = "0" * (len(N) - len(str(int(N))) - 1) + M
        else:
            N = M
    print(c)