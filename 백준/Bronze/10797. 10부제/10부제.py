n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for elt in arr:
    if elt == n:
        cnt += 1
        
print(cnt)