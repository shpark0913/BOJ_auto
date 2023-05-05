import sys
input = sys.stdin.readline

# 메시지의 길이 N, 숫자의 최댓값 C
N, C = map(int, input().split())

# 숫자들의 빈도수를 나타내는 딕셔너리
numsDic = {}

numsList = list(map(int, input().split()))

for num in numsList:
    if num in numsDic.keys():
        numsDic[num] += 1
    else:
        numsDic[num] = 1

# numsDic을 .items()를 활용해 list로 변경, 이후 2번째 원소로 정렬
numsDic = sorted(numsDic.items(), key=lambda x:-x[1])

# 문제에서 요구하는 순서로 정렬된 리스트
ansList = []

for num in numsDic:
    for _ in range(num[1]):
        ansList.append(num[0])

print(*ansList)