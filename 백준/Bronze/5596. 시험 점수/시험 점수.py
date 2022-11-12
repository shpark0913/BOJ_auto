N = map(int, input().split())

M = map(int, input().split())

S = sum(N)
T = sum(M)

print(S) if S >= T else print(T)