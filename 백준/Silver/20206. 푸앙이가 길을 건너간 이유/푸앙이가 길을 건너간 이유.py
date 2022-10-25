A, B, C = map(int, input().split())

X1, X2, Y1, Y2 = map(int, input().split())


def f(X):
    global A, B, C
    return -1 * (A*X + C) / B

if not A:
    print("Poor") if Y1 < -1 * (C / B) < Y2 else print("Lucky")

elif not B:
    print("Poor") if X1 < -1 * (C / A) < X2 else print("Lucky")

else:
    print("Poor") if (((f(X1) - Y1) * (f(X2) - Y2) < 0) or ((f(X1) - Y2) * (f(X2) - Y1) < 0)) else print("Lucky")
