s = input()
s = s.upper()
dic = {}
for i in s:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
max_num = max(dic.values())
cnt = 0
for elt in dic.keys():
    if dic[elt] == max_num:
        max_elt = elt
        cnt += 1
if cnt == 1:
    print(max_elt)
else:
    print('?')