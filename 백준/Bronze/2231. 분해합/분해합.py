N = int(input())

res = N // 2

while 1:
    ans = res
    if ans > N:
        print(0)
        exit(0)
    for i in range(len(str(res))):
        ans += int(str(res)[i])
    if ans == N:
        print(res)
        exit(0)
    res += 1