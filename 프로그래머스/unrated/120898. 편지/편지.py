def solution(message):
    message = list(message.split())
    ans = ""
    for m in message:
        ans += m
        ans += " "
    print(ans)
    answer = (len(ans) * 2 - 2)
    return answer