N, M = map(int, input().split())

lstA = []
lstAA = []
lstB = []

for _ in range(N):
    lstA.append(input())

for _ in range(N):
    lstB.append(input())

for elt in lstA:
    ans = ""
    for i in range(M):
        for _ in range(2):
            ans += elt[i]
    lstAA.append(ans)

if lstAA == lstB:
    print("Eyfa")
else:
    print("Not Eyfa")