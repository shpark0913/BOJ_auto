N = int(input())
scores = list(map(int, input().split()))
scores.sort()

for i in range(len(scores)):
    scores[i] = (100 * scores[i] / scores[-1])
print(sum(scores)/N)