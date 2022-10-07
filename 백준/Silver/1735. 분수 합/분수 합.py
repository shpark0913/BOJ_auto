from fractions import Fraction         # 소수가 아니라 분수 표현을 위해 사용

A1, B1 = map(int, input().split())

A2, B2 = map(int, input().split())

Q1 = Fraction(A1, B1)
Q2 = Fraction(A2, B2)

print((Q1+Q2).numerator, (Q1+Q2).denominator)
