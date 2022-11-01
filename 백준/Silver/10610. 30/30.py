N = list(map(int, input()))

N_list = sorted(N, reverse=True)

if N_list[-1] or sum(N_list) % 3:
    print(-1)
else:
    s = ''
    for elt in N_list:
        s += str(elt)
    print(s)