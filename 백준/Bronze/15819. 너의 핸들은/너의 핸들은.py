N, I = map(int, input().split())

handles = []

for _ in range(N):
    handles.append(input())

handles.sort()

print(handles[I-1])