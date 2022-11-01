s = []
for _ in range(K := int(input())):
    s.append(n) if (n := int(input())) else s.pop()
print(sum(s))