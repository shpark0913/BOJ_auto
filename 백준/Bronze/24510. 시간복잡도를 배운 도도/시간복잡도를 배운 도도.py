m = 0
for _ in range(int(input())):
    s = input()
    cf = s.count('for')
    cw = s.count('while')
    if m < cf + cw:
        m = cf + cw
print(m)