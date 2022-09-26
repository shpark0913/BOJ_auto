N = int(input())

lst = [input() for _ in range(N)]
arr = []
for s in lst:
    s = '0' + s
    word = ''
    # print(s)
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            word += s[i]
    arr.append(word)
c = N
for elt in arr:
    dic = {}
    for i in elt:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.values():
        if i > 1:
            c -= 1
            break
print(c)