# 배달해야 할 설탕 무게
N = int(input())
lst = [N]
# 5kg 봉지의 수 (3kg 봉지의 수는 num3)
num5 = N//5

while 1:
    N = lst[0]
    if num5 < 0:
        print(-1)
        break
    N -= (5 * num5)
    num3 = (N // 3)
    N %= 3
    if N == 0:
        print(num5 + num3)
        break
    num5 -= 1