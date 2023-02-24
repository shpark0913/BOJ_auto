fruitNum, snakeLen = list(map(int, input().split()))

fruitsHeigth = sorted(list(map(int, input().split())))

for i in range(len(fruitsHeigth)):
    if snakeLen >= fruitsHeigth[i]:
        snakeLen += 1
    else: break

print(snakeLen)