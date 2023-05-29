# N : 카드의 개수, M : 딜러가 부른 수
N, M = map(int, input().split())

cards = sorted(list(map(int, input().split())), reverse=True)

candidates = []

for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            candidates.append(cards[i] + cards[j] + cards[k])

candidates.sort(reverse=True)

for candidate in candidates:
    if candidate <= M:
        print(candidate)
        exit(0)