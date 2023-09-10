for _ in range(int(input())):
    N, M = map(int, input().split())
    ans = 0
    for i in range(N, M + 1):
        for j in str(i):
           if j == "0":
               ans += 1
    print(ans)