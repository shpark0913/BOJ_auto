K = int(input())
stack = []

for _ in range(K):
    stack.append(n) if (n := int(input())) else stack.pop()
print(sum(stack))