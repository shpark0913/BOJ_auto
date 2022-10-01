N = int(input())
have = list(map(int, input().split()))
have_dic = {}

for elt in have:
    have_dic[elt] = '1 '

M = int(input())
wonder = list(map(int, input().split()))

ans = ''
for elt in wonder:
    ans += have_dic.get(elt, '0 ')

print(ans)