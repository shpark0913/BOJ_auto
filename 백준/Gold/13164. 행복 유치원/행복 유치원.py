childNum, groupNum = map(int, input().split())

childHeights = list(map(int, input().split()))

# 계차수열 (키의 차이를 나타냄)
differHeights = []

# 계차수열을 내림차순으로
differHeights_order = []

for i in range(len(childHeights)-1):
    differHeights.append(childHeights[i+1]-childHeights[i])
differHeights_order = sorted(differHeights, reverse=True)

# groupNum 개의 조로 나누고 싶다
makeGroups = []

for i in range(groupNum-1):
    makeGroups.append(differHeights_order[i])


print(sum(differHeights) - sum(makeGroups))