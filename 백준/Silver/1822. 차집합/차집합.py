import sys
input = sys.stdin.readline

numA, numB = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
AminusB = list(setA - setB)

if AminusB:
    print(len(AminusB))
    print(*sorted(AminusB))

else:
    print(0)