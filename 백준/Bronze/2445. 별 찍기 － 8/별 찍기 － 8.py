N = int(input())

for i in range(1, N+1):
    s = ''
    if i <= N:
        s += '*'*i
    s += ' '*(N-i)

    print(s, end ='')
    print(s[::-1])

for i in range(N-1, 0, -1):
    s = ''
    if i <= N:
        s += '*'*i
    s += ' '*(N-i)

    print(s, end ='')
    print(s[::-1])