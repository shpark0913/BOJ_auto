N = str(input())
L = len(N)
N = int(N)

cnt = 0

for i in range(L-1):
    cnt += (i+1)*(10**(i+1) - 10**(i))

num = N - 10**(L-1) + 1

cnt += num*L

print(cnt%1234567)