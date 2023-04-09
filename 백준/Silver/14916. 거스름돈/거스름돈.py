# 거스름돈 액수
change = int(input())

# 2원, 5원의 개수 : coin2, coin5
coin2 = 0
coin5 = change // 5

# 전체 거스름돈에서 5원 동전을 거스르고 남은 액수
remainder = change - 5 * coin5

while 1:
    # 5원의 개수가 음수라면 거스름돈 주기 실패
    if coin5 < 0:
        print(-1)
        exit(0)
    # 남은 돈이 2의 배수라면 거스름돈 주기 성공
    if not remainder % 2:
        coin2 = remainder // 2
        print(coin2 + coin5)
        exit(0)
    coin5 -= 1
    remainder += 5