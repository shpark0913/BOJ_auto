# 로프의 개수
N = int(input())

# 로프들이 각각 들 수 있는 물체의 중량
canLift = []

for _ in range(N):
    canLift.append(int(input()))

canLift = sorted(canLift)

maxCanLift = 0

for i in range(len(canLift)):
    weight = canLift[i] * (len(canLift) - i)
    if weight > maxCanLift:
        maxCanLift = weight

print(maxCanLift)