N = list(map(int, input()))

N_list = sorted(N, reverse=True)

if N_list[-1] or sum(N) % 3:
    print(-1)

else:
    for elt in N_list:
        print(elt, end='')