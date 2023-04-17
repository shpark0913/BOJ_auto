# 줄을 서 있는 모든 사람의 수
N = int(input())

# 각 사람이 인출하는데 걸리는 시간
moneyTime = list(map(int, input().split()))

moneyTime.sort()

# 답을 allTime이라는 변수에 넣자
allTime = 0

for i in range(len(moneyTime)):
    allTime += (len(moneyTime) - i)*moneyTime[i]

print(allTime)