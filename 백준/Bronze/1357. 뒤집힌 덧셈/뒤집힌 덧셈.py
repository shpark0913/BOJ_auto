def Rev(x):
    return int(x[::-1])

X, Y = input().split()

print(Rev(str(Rev(X)+Rev(Y))))