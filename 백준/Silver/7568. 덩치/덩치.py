# 사람의 수
N = int(input())

# N명의 몸무게, 키를 원소로 가지는 리스트
people = []
for _ in range(N):
   people.append(list(map(int, input().split())))

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")