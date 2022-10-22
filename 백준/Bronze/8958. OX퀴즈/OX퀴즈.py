T = int(input())

for t in range(T):
    S = input()
    score = 0
    cnt = 0
    for i in S:
        if i == 'O':
            cnt += 1
            score += cnt
        elif i == 'X':
            cnt = 0
    print(score)