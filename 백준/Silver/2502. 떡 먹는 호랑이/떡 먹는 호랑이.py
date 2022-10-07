D, K = map(int, input().split())

def f():
    global D
    global K
    ricecake = [0] * (D + 1)
    ricecake[D] = K
    while 1:
        for i in range(1, K):
            ricecake[D-1] = K-i
            for j in range(2, D):
                ricecake[D-j] = ricecake[D-(j-2)] - ricecake[D-(j-1)]
                if ricecake[D-j] > ricecake[D-(j-1)]:
                    continue
            a = sorted(ricecake)
            if a == ricecake:
                print(ricecake[1])
                print(ricecake[2])
                return

f()