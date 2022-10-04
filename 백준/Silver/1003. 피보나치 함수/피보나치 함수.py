lst = [
    [1, 0],
    [0, 1],
    [1, 1]
]
for i in range(3, 41):
    lst.append([lst[i-2][0] + lst[i-1][0], lst[i-2][1] + lst[i-1][1]])

T = int(input())
for t in range(T):
    N = int(input())
    print(*lst[N])