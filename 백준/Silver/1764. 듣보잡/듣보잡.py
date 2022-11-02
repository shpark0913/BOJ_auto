N, M = map(int, input().split())

D = {input() for _ in range(N)}

B = {input() for _ in range(M)}

BD = sorted(list(B & D))
print(len(BD))
for i in BD:
    print(i)