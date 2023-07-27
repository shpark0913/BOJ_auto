S = input()

answers = []

for i in range(len(S)):
    answers.append(S[i::])

answers.sort()
print(*answers)
