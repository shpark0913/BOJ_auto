s = input()
t = input()

if len(s) < len(t):
    M = t
    m = s
else:
    M = s
    m = t

len_M = len(M)
len_m = len(m)

if m*len_M == M*len_m:
    print(1)
else: print(0)