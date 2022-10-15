N1 = int(input())

N2 = N1 % 16

if N2 >= 10:
    N2 -= 8

elif N2 == 0:
    N2 = 8

if N2 in {1, 9}:
    print(1)

elif N2 in {2, 8}:
    print(2)

elif N2 in {3, 7}:
    print(3)

elif N2 in {4, 6}:
    print(4)

elif N2 == 5:
    print(5)