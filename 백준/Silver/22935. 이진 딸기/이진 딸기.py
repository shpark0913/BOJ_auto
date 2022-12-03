for t in range(int(input())):
    N = int(input()) % 28
    if not N:
        N = 2
    elif N > 15:
        N = 30 - N
    binary_N = ''
    cnt = 1
    while N:
        if N % 2:
            binary_N = '딸기' + binary_N
            N = N//2
            cnt += 1
        else:
            binary_N = 'V' + binary_N
            N = N//2
            cnt += 1
    if cnt == 5:
        print(binary_N)
    else:
        print('V'*(5 - cnt) + binary_N)