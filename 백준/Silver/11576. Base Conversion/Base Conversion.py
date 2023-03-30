A, B = map(int, input().split())

n = int(input())

# numA : A진법으로 표현된 수
numA = list(map(int, input().split()))

# num10 : numA를 10진법으로 바꾼 수
num10 = 0

for i in range(n):
    num10 += (numA[i]*(A**(n - 1 - i)))

numB = []

while num10:
    numB.append(num10 % B)
    num10 //= B

print(*numB[::-1])