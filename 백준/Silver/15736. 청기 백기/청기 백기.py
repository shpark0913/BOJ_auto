windows = 0
N = int(input())
num = 1
while 1:
    if num**2 <= N:
        windows += 1
        num += 1
    else: break
print(windows)