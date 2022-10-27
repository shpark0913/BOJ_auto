N = str(input())
L = len(N)
cnt = 0

if L == 1:
    cnt = int(N)
else:
    for i in range(1, L):
        cnt += i * (10**i - 10**(i-1))
    cnt += L*(int(N) - 10**(L-1) + 1)

print(cnt)