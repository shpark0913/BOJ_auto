import sys
input = sys.stdin.readline

# 프로젝트 팀의 수
teamNums = int(input())

#  모든 학생들의 코딩 역량
scores = sorted(list(map(int, input().split())))

if teamNums == 1:
    print(sum(scores))
    exit(0)

# 코딩 역량이 최소인 팀의 점수 (초기에는 큰 값을 부여해 최솟값을 찾기 용이하게 함)
minScore = scores[-1] * teamNums

for i in range(teamNums):
    if minScore > scores[i] + scores[- i - 1]:
        minScore = scores[i] + scores[- i - 1]

print(minScore)