import sys
input = sys.stdin.readline

N = int(input())

names = input().split()
stuLikes = {}
for name in names:
    stuLikes[name] = 0

for _ in range(N):
    stuLike = input().split()
    for stu in stuLike:
        stuLikes[stu] += 1

for stu in sorted(stuLikes, key=lambda x:-stuLikes[x]):
    print(stu, stuLikes[stu])