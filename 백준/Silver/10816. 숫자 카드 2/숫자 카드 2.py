N = int(input())
total_card = list(map(int, input().split()))
M = int(input())
want_card = list(map(int, input().split()))
dic = {}
lst = []
for elt in total_card:
    if elt in dic.keys():
        dic[elt] += 1
    else:
        dic[elt] = 1
for elt in want_card:
    if elt in dic.keys():
        lst.append(dic[elt])
    else:
        lst.append(0)
print(*lst)