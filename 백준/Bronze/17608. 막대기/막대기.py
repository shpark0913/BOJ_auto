sticks = []
cnt = 1
for _ in range(N:=int(input())):
    sticks.append(int(input()))

now = sticks[-1]

for i in range(len(sticks)-1, -1, -1):
    if now < sticks[i]:
        now = sticks[i]
        cnt += 1

print(cnt)