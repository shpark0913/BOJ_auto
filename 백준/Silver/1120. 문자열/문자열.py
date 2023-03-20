m, n = input().split()

ans = []
for i in range(len(n) - len(m) + 1):
    cnt = 0
    for j in range(len(m)):
        if m[j] != n[i + j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))