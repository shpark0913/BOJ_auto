import sys
input = sys.stdin.readline

# 참가자의 수
N = int(input())

# 해결한 문제 수와 페널티
information = []

for _ in range(N):
    information.append(list(map(int, input().split())))

information.sort(key = lambda x :(-x[0], x[1]))

# 5등 참가자
person5th = information[4]

# 5등 참가자와 해결한 문제 수가 같은 학생들을 원소로 가지는 리스트
infor_5th = []

for elt in information:
    if elt[0] == information[4][0] and elt[1] > information[4][1]:
        infor_5th.append(elt)

print(len(infor_5th))