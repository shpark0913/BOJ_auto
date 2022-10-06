a, m = map(int, input().split())

x = 0
while 1:
    x += 1
    res = (a*x - 1) % m
    if res == 0:
        print(x)
        break