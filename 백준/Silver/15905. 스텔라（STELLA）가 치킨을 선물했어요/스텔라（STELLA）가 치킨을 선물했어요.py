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

# 5등 참가자와 해결한 문제 수가 같지만 수상을 못한 학생의 수
cnt = 0

for i in range(5, len(information)):
    if information[i][0] < person5th[0]:
        break
    cnt += 1
    
print(cnt)