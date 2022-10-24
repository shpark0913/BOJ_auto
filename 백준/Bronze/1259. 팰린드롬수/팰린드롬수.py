while 1:
    if (n:=str(input()))=='0':break
    m=list(map(int, n))
    print('yes') if m==m[::-1] else print('no')