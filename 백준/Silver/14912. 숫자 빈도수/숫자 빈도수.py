n, d = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    str_i = str(i)
    for elt in str_i:
        if str(d) == elt:
            cnt += 1

print(cnt)