while 1:
    if (n:=str(input()))=='0':break
    m=list(map(int, n))
    p=m[::-1]
    print('yes') if m==p else print('no')