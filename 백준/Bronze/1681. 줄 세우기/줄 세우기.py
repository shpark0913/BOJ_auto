A, B = input().split()
N = int(A)
c = 0
n = 0
while c != N:
    n += 1
    if B in str(n):
        continue
    c += 1
print(n)