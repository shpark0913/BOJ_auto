from collections import deque

A, B = map(int, input().split())
ans = -1
queue = deque([(A, 1)])

while queue:
    a, b = queue.popleft()
    if a == B:
        ans = b
        break
        
    if a * 2 <= B:
        queue.append((a*2, b + 1))
    if int(str(a) + "1") <= B:
        queue.append((int(str(a) + '1'), b + 1))
        
print(ans)