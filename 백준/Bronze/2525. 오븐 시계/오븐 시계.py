H, M = map(int, input().split())
t = int(input()) 

H += t // 60
M += t % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)