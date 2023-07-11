for _ in range(int(input())):
    s, p = input().split()
    cnt = s.count(p)
    print(len(s) - cnt * len(p) + cnt)
