# 소의 수
N = int(input())

# 각 소의 도착 시간과 검문 시간
cows = []

for i in range(N):
    arriveTime, inspectTime = map(int, input().split())
    cows.append([arriveTime, inspectTime])

# 도착 시간 순서로 정렬
cows.sort(key=lambda x:x[0])

# 모든 소가 입장하는데 총 소요 시간
entireTime = 0

for i in range(N):
    arrive, inspect = cows[i]
    if entireTime < arrive:
        entireTime = arrive + inspect
    else:
        entireTime += inspect

print(entireTime)