scores = [[0]]

for _ in range(K := int(input())):
    scores.append(list(map(int, input().split())))

for i in range(1, K+1):
    print(f'Class {i}')
    stuNums = scores[i].pop(0)
    scores[i].sort()
    largestGap = 0
    for j in range(stuNums-1):
        if largestGap < scores[i][j+1] - scores[i][j]:
            largestGap = scores[i][j+1] - scores[i][j]
    print(f'Max {scores[i][-1]}, Min {scores[i][0]}, Largest gap {largestGap}')