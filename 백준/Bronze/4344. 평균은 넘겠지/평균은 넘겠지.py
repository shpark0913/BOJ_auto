C = int(input())

for _ in range(C):
    test = list(input().split())
    test_score = []
    for i in range(1, len(test)):
        test_score.append(int(test[i]))
    avg = sum(test_score)/len(test_score)

    exceed_avg = 0

    for score in test_score:
        if score > avg:
            exceed_avg += 1

    ans = str(round(exceed_avg/len(test_score), 5))

    ans_percent = ""

    i = 2
    while 1:
        try:
            ans_percent += ans[i]
        except:
            ans_percent += "0"
        if i == 3:
            ans_percent += "."
        if i == 6:
            ans_percent += "%"
            break
        i += 1

    print(ans_percent)