def solution(s):
    lst = list(s.split(" "))
    new_lst = []
    for l in lst:
        new_l = ""
        for i in range(len(l)):
            if not i % 2:
                new_l += l[i].upper()
            else:
                new_l += l[i].lower()
        new_lst.append(new_l)
    answer = new_lst[0]
    for i in range(1, len(new_lst)):
        answer += (" " + new_lst[i])
    return answer