import sys

while 1:
    n, k = map(int, sys.stdin.readline().split())
    if {n, k} == {0}:
        break
    a, b = 1, 1
    j = n - k
    for i in range(n, max(k, j), -1):
        a *= i
    for i in range(min(k, j), 0, -1):
        b *= i
    print(a//b)