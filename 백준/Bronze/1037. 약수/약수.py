N=int(input())
l=sorted(list(map(int,input().split())))
print(l[0]**2) if len(l)==1 else print(l[0]*l[-1])