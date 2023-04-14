# 참가자의 점수와 문제 번호를 원소로 가지는 이중 리스트
scores = []

for i in range(1, 9):
    scores.append([int(input()), i])

# 참가자의 점수 내림차순으로 이중 리스트 구성
scores.sort(key=lambda x:-x[0])

# 상위 5개 점수의 합
scoreNum = 0

# 상위 5개 점수 문제의 번호를 가지는 리스트
scoreList = []

for i in range(5):
    scoreNum += scores[i][0]
    scoreList.append(scores[i][1])

print(scoreNum)
print(*sorted(scoreList))
