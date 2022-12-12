N = int(input())

if not (N//3)%2:
    if N%3 == 1: print("SK")
    else: print("CY")
else:
    if N%3 == 1: print("CY")
    else: print("SK")