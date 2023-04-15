lst = [0]

for i in range(0, 50):
    for j in range(i):
        lst.append(i)

s, e = map(int, input().split())

ans = 0
for i in range(s, e+1):
    ans += lst[i]

print(ans)