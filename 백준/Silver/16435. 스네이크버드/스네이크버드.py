# fruitNum : 과일의 개수, snakeLen : 뱀의 처음 길이
fruitNum, snakeLen = list(map(int, input().split()))

# 과일의 높이를 순서대로 나타낸 list
fruitsHeigth = sorted(list(map(int, input().split())))

# 과일 높이가 뱀 높이 이하이면 뱀 높이 +1, 그렇지 않다면 for문 종료
for i in range(len(fruitsHeigth)):
    if snakeLen >= fruitsHeigth[i]:
        snakeLen += 1
    else: break

print(snakeLen)