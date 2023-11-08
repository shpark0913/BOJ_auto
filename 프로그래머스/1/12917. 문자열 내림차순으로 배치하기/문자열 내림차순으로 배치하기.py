def solution(s):
    s_list = list(s)
    s_list.sort(reverse=True)
    answer = ''
    for elt in s_list:
        answer += elt
    return answer