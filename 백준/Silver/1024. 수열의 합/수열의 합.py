N, L = map(int, input().split())

while 1:
    a = (1-L)/2 + N/L
    if a < 0 or L > 100:
        print(-1)
        break
    if a == int(a):
        for i in range(L):
            print(int(a + i), end=' ')
        break
    else:
        L += 1