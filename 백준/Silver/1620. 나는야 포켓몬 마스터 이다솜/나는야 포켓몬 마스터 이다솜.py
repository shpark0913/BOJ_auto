N, M = map(int, input().split())
monster = {}
monster2 = {}
cnt = 0
for _ in range(N):
    cnt += 1
    monster[cnt] = input()
for a, b in monster.items():
    monster2[b] = a

for _ in range(M):
    n = input()
    if n.isdigit():
        print(monster[int(n)])
    else:
        print(monster2[n])
