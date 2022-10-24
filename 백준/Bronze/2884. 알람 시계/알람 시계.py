H, M = map(int, input().split())

def f():
    global H, M
    M -= 45
    if M >= 0:
        print(H, M)
        return
    elif M < 0:
        M += 60
        H -= 1
        if H >= 0:
            print(H, M)
            return
        else:
            H = 23
            print(H, M)
            return

f()