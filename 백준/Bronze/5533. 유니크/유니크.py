N = int(input())

first = []
second = []
third = []

for _ in range(N):
    a, b, c = map(int, input().split())
    first.append(a)
    second.append(b)
    third.append(c)

scores = [0] * N

for i in range(N):
    score = 0
    a = first.count(first[i])
    b = second.count(second[i])
    c = third.count(third[i])
    if a == 1:
        score += first[i]
    if b == 1:
        score += second[i]
    if c == 1:
        score += third[i]
    scores[i] = score

for score in scores:
    print(score)