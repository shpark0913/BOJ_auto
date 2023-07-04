def cnt(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return cnt(n - 1) + cnt(n - 2) + cnt(n - 3)


for _ in range(T := int(input())):
    print(cnt((n := int(input()))))
