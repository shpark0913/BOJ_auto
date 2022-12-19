N, M = map(int, input().split())

DNAS = [input() for _ in range(N)]
s = ''
cnt = 0

for i in range(M):
    nuc = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for DNA in DNAS:
        nuc[DNA[i]] += 1
    num = 0
    word = 'A'
    for key, value in nuc.items():
        if num < value:
            num = value
            word = key
    s += word

for DNA in DNAS:
    for i in range(M):
        if DNA[i] != s[i]: cnt += 1

print(s)
print(cnt)