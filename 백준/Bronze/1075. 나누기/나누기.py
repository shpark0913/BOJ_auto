N = int(input())
F = int(input())
N = (N // 100) * 100
while 1:
    if N % F:
        N += 1
    else:
        break
N = str(N)
print(N[-2:])