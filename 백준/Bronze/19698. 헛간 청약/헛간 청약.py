N, W, H, L = map(int, input().split())

a = (W//L)*(H//L)

if a >= N:
    print(N)
else:
    print(a)