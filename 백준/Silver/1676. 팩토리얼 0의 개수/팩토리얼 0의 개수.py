N = int(input())

n = 1
for i in range(1, N+1):
    n *= i
n = str(n)
cnt = 0
for i in n[::-1]:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)