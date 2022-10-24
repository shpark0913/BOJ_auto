from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    order = input().rstrip('\n')
    if order == 'pop':
        print(queue.popleft()) if queue else print(-1)

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        print(0) if queue else print(1)

    elif order == 'front':
        print(queue[0]) if queue else print(-1)

    elif order == 'back':
        print(queue[-1]) if queue else print(-1)

    else:
        order = int(order[5:])
        queue.append(order)