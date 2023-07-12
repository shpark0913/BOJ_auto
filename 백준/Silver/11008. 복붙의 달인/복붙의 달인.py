for _ in range(int(input())):
    s, p = input().split()
    cnt = s.count(p)
    print(len(s) + cnt * (1 - len(p)))
