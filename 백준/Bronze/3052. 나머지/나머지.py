numbers = [int(input()) for _ in range(10)]
res = []
for i in numbers:
    I = i%42
    if I not in res:
        res.append(I)
print(len(res))