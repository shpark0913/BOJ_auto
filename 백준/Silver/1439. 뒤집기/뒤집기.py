S = input()

S_0 = list(S.split('0'))
S_1 = list(S.split('1'))

cnt_0 = 0
cnt_1 = 0

for elt in S_0:
    if elt: cnt_0 += 1

for elt in S_1:
    if elt: cnt_1 += 1

if S == S_0[0] or S == S_1[0]:
    print(0)
else: print(min(cnt_0, cnt_1))