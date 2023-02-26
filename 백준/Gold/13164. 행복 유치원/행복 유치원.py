import sys
input = sys.stdin.readline

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

# 3조로 나누고 싶으면 2 부분을 나눠야 하므로 range 내부에 -1 해줌
for i in range(groupNum-1):
    makeGroups.append(differHeights_order[i])

# 모든 학생의 키 합에서 계차수열의 큰 숫자들을 뺀다
print(sum(differHeights) - sum(makeGroups))