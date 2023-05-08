import sys
input = sys.stdin.readline

# N : 리스트에 있는 점수의 개수, P : 랭킹 리스트에 올라갈 수 있는 점수의 개수
N, newScore, P = map(int, input().split())
scoreList = list(map(int, input().split()))

sameScore = -1
orderNum = 0
peopleNum = 0

if N == 0:
    print(1)
    exit(0)

for score in scoreList:
    if score < newScore: break
    elif score == newScore:
        sameScore += 1
        orderNum += 1
    else: orderNum += 1
    peopleNum += 1

newOrder = orderNum - sameScore

if peopleNum < P:
    print(newOrder)
else:
    print(-1)