T = int(input())

for t in range(T):
    R, S = input().split()
    s = ''
    for i in S:
        s += (str(i) * int(R))
    print(s)