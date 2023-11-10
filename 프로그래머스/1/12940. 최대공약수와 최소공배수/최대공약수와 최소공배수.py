import math

def solution(n, m):
    answer = []
    g = math.gcd(n, m)
    l = int(g * (n // g) * (m // g))
    answer.append(g)
    answer.append(l)
    return answer