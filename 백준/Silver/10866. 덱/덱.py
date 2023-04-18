import sys
# 명령의 수
N = int(input())

deque = []

for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if "push_front" in order:
        a, b = order.split()
        if deque:
            deque = [int(b)] + deque
        else:
            deque = [int(b)]
    elif "push_back" in order:
        a, b = order.split()
        if deque:
            deque = deque + [int(b)]
        else:
            deque = [int(b)]
    elif order == "pop_front":
        if deque:
            a = deque.pop(0)
            print(a)
        else:
            print(-1)
    elif order == "pop_back":
        if deque:
            a = deque.pop(-1)
            print(a)
        else:
            print(-1)
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif order == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif order == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)