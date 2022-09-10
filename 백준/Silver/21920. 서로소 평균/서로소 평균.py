import math
N = int(input())
lst = list(map(int,input().split()))
X = int(input())
c = 0
num = 0
for elt in lst:
    if math.gcd(X, elt) == 1:
        c += elt
        num += 1
    else:
        pass
print(c/num)