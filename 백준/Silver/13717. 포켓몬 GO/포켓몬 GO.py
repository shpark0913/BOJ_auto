# 포켓몬의 총 마리수
N = int(input())

pocketmons = []
for _ in range(N):
    name = input()
    candyNeed, candyHave = map(int, input().split())
    canEvolution = 0
    while 1:
        if candyHave < candyNeed:
            break
        canEvolution += 1
        candyHave = candyHave - candyNeed + 2
    pocketmons.append([name, canEvolution])

maxValue = pocketmons[-1][1]
allEvolution = 0
pocketmon = ''
for i in range(len(pocketmons)-1, -1, -1):
    allEvolution += pocketmons[i][1]
    if pocketmons[i][1] >= maxValue:
        maxValue = pocketmons[i][1]
        pocketmon = pocketmons[i][0]

print(allEvolution)
print(pocketmon)