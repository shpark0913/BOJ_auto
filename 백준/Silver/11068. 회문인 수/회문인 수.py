def ftn(a, b):
    ans = []
    while a > 0:
        ans.append(a % b)
        a //= b
    ans = ans[::-1]
    return ans

def pal(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return 0
    return 1

t = int(input())

for _ in range(t):
    cnt = 0
    n = int(input())
    for i in range(2, 65):
        if pal(ftn(n, i)):
            cnt = pal(ftn(n, i))
            break
    print(1) if cnt else print(0)
