A, B = map(int, input().split(':'))

minV, maxV = min(A, B), max(A, B)

divisors = []

for i in range(1, int(minV**(1/2)) + 1):
    if not (minV % i):
        divisors.append(i)
        divisors.append(minV//i)
divisors.sort(reverse=True)

for divisor in divisors:
    if not maxV % divisor:
        common_divisor = divisor
        break

if common_divisor:
    print(str(A//common_divisor)+':'+str(B//common_divisor))
else:
    print(str(A)+':'+str(B))