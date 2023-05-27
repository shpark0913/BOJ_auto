N = int(input())

def game(num):

    # True : 상근이 차례, False : 창영이 차례
    turn = True

    while 1:
        if num <= 0:
            print("SK") if turn else print("CY")
            break
        if num > 3:
            num -= 3
        else:
            num -= 1

        if turn:
            turn = False
        else:
            turn = True

game(N)