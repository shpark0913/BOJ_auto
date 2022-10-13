N = int(input())

def facto(n):
    if n <= 1:
        return 1
    else:
        return n*facto(n-1)

if N < 4:
    print(0)
else:
    print(facto(N)//(facto(4)*facto(N-4)))