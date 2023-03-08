N = int(input())

# 컵 위치 변경 횟수
changeNum = int(N/2)

ans = 1

for i in range(1, changeNum + 1):
    ans *= ( 2 * i - 1 )

print(ans % (10**9+7))