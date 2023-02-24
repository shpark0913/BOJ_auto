#  궁금한 문자열
strWonder = input()

# 문자열이 포함된 반지의 개수
cnt = 0

# ring : 반지의 문자열 
# ringWords : 반지의 문자열을 2번 반복한 것 (반지는 시작과 끝이 연결되었으므로)
for _ in range(ringNums := int(input())):
    ring = input()
    ringWords = ring * 2
    if strWonder in ringWords:
        cnt += 1

print(cnt)