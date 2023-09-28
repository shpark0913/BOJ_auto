N = int(input())

c = [1,2,3]
for _ in range(N):
    x, y = map(int, input().split())
    
    X = c.index(x)
    Y = c.index(y)
    
    c[X], c[Y] = c[Y], c[X]
    
print(c[0])