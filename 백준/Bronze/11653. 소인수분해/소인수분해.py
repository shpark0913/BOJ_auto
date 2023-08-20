N = int(input())

if N == 1:
    print("")
    exit(0)

ans = []

for i in range(2, N + 1):
    if not N % i:
        while not N % i:
            print(i)
            N = N / i
