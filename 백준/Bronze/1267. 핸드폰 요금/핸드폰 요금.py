import sys
input = sys.stdin.readline

N = int(input())

calls = list(map(int, input().split()))

Y, M = 0, 0

for call in calls:
    Y += (1 + call//30)*10
    M += (1 + call//60)*15

if Y < M:
    print("Y", Y)
elif Y > M:
    print("M", M)
else:
    print("Y", "M", Y)