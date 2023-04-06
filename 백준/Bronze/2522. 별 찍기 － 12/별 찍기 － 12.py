N = int(input())

for i in range(1, N+1):
    stars = ' '*(N-i) + '*'*i
    print(stars)
for i in range(N-1, 0, -1):
    stars = ' '*(N-i) + '*'*i
    print(stars)