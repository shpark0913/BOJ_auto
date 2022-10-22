A = [n := int(input()) for _ in range(9)]
a = max(A)
for i in range(len(A)):
    if A[i] == a:
        print(a)
        print(i+1)
