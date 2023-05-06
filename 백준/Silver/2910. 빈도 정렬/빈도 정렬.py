import sys
input = sys.stdin.readline

N, C = map(int, input().split())
numsList = list(map(int, input().split()))

numsDic = {}

for num in numsList:
    try:
        numsDic[num] += 1
    except:
        numsDic[num] = 1

numsDic = sorted(numsDic.items(), key=lambda x:x[1], reverse=True)

for num in numsDic:
    for _ in range(num[1]):
        print(num[0], end=" ")
