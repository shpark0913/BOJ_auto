import sys
input = sys.stdin.readline

# 회원의 수
N = int(input())

# 회원들의 나이, 이름
members = []
for _ in range(N):
    # age를 숫자, name을 문자로 설정
    age, name = input().split()
    age = int(age)
    members.append([age, name])

# 멤버들을 나이가 증가하는 순으로
# 나이가 같다면 먼저 가입한 순으로 정렬
members.sort(key=lambda x:x[0])

for member in members:
    print(*member)

