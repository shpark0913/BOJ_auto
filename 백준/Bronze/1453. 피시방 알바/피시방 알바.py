n = int(input())
arr = list(map(int, input().split()))
c = 0
s = []
for i in range(n):
    if arr[i] in s:
        c += 1 
    else:                      
        s.append(arr[i])  
print(c)