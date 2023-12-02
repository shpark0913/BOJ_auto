def solution(k, scores):
    answer = []
    ans = []
    for score in scores:
        answer.append(score)
        answer.sort()
        if len(answer) > k:
            answer = answer[1:]
        ans.append(answer[0])
    return ans