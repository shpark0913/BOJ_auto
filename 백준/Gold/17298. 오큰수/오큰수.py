N = int(input())
lst = list(map(int, input().split()))
stack = []

for i in range(N):
    while stack:
        if lst[i] > lst[stack[-1]]:
            lst[stack.pop()] = lst[i]
        else:
            stack.append(i)
            break
    if not stack:
        stack.append(i)
for i in stack:
    lst[i] = -1

print(*lst)