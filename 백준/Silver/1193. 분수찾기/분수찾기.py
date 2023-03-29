# X번째 분수를 구하여라
X = int(input())

n = 1
while 1:
    if (n**2 - n + 2)/2 <= X < ((n+1)**2 - (n + 1) + 2)/2:
        break
    n += 1

diff = X - int((n**2 - n + 2)/2)

num = str(1 + diff)
den = str(n - diff)

if n % 2:
    print(den + "/" + num)
else:
    print(num + "/" + den)
