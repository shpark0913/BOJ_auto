A, B = map(str, input().split())
newA, newB = "", ""

for i in range(len(A)):
    if A[i] == "5":
        newA += "6"
    else:
        newA += A[i]

for i in range(len(B)):
    if B[i] == "5":
        newB += "6"
    else:
        newB += B[i]


max_value = int(newA) + int(newB)

newA, newB = "", ""

for i in range(len(A)):
    if A[i] == "6":
        newA += "5"
    else:
        newA += A[i]

for i in range(len(B)):
    if B[i] == "6":
        newB += "5"
    else:
        newB += B[i]

min_value = int(newA) + int(newB)

print(min_value, max_value)