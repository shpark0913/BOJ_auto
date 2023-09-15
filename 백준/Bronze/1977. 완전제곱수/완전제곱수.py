M = int(input())
N = int(input())
sum = 0
min = 0
for i in range(1, 101):
    if M <= i ** 2 and N >= i ** 2:
        if sum == 0:
            min = i ** 2
        sum += i ** 2

if not sum:
    print(-1)
else:
    print(sum)
    print(min)