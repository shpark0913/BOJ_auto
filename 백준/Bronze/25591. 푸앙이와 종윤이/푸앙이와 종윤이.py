c1, c2 = map(int, input().split())

a = 100 - c1
b = 100 - c2
c = 100 - a - b
d = a * b

q = d//100
r = d%100
print(a, b, c, d, q, r)
if d >= 10:
    print(c+q, r)
else:
    print(c, d)