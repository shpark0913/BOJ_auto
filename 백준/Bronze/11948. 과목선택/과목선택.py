A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
sum = 0
sum = sum + A + B + C + D - min(A, B, C, D)
sum = sum + E + F - min(E, F)

print(sum)