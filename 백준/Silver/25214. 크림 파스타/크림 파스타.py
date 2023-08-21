N = int(input())

scores = list(map(int, input().split()))

max_score_diff = [0]

min_value = scores[0]

for i in range(1, len(scores)):
    if scores[i] < min_value:
        min_value = scores[i]
    diff = max(scores[i] - min_value, max_score_diff[i - 1])
    max_score_diff.append(diff)

print(*max_score_diff)