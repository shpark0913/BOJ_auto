l = []

for _ in range(int(input())):
    l.append(int(input()))
    
ans = l[-1]
if l[2]-l[1] == l[1]-l[0]:
    ans += (l[1]-l[0])
elif l[2]//l[1] == l[1]//l[0]:
    ans *= (l[1]//l[0])

print(ans)