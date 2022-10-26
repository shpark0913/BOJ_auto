T = int(input())

def f(n):
    return 1 + n * (n - 1) // 2


def findfunc(X):
    n = 1
    while 1:
        if X == 1:
            group = 1
            start_num = 1
            return group, start_num
        if f(n) <= X < f(n + 1):
            group = n
            start_num = f(n)
            return group, start_num
        else:
            n += 1

for t in range(T):
    N1, N2 = map(int, input().split())
    group1, start_num_1 = findfunc(N1)
    group2, start_num_2 = findfunc(N2)

    sum1, sum2 = group1 + 1, group2 + 1

    N1_X, N1_Y = 1 + N1 - start_num_1, sum1 - 1 - N1 + start_num_1
    N2_X, N2_Y = 1 + N2 - start_num_2, sum2 - 1 - N2 + start_num_2

    X, Y = N1_X + N2_X, N1_Y + N2_Y
    GROUP = X + Y

    print(f(GROUP-1) + (X-1))
