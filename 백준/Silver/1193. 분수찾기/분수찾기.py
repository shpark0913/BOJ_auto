X=int(input())
n=1
while 1:
    if (n**2 - n + 2)/2 <= X < ((n+1)**2 - (n + 1) + 2)/2:break
    n += 1
d=X-int((n**2-n+2)/2)
w=str(1+d)
p=str(n-d)
print(p+"/"+w) if n%2 else print(w+"/"+p)
