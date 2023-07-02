K=int(input())
d=[[] for _ in range(K+1)]
d[0]=[1, 0]
for i in range(1,K+1):
    A,B=d[i-1][0],d[i-1][1]
    d[i]=B,A+B
print(*d[i])