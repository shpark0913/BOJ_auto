N = int(input())
have = list(map(int, input().split()))
have_dic = {}

for elt in have:
    have_dic[elt] = 1

M = int(input())
wonder = list(map(int, input().split()))

for elt in wonder:
    if elt in have_dic.keys():
        print(1, end = ' ')
    else:
        print(0, end = ' ')