N, L, H = map(int, input().split())

scores = list(map(int, input().split()))

scores.sort()

new_scores = sorted(scores[L:], reverse=True)

print(sum(new_scores[H:])/len(new_scores[H:]))