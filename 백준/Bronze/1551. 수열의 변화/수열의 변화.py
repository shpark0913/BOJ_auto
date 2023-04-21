N, K = map(int, input().split())

lst = list(map(int, input().split(",")))

for i in range(K):
    lst2 = []
    for i in range(len(lst)-1):
        lst2.append(lst[i+1]-lst[i])
    lst = lst2

for i in range(len(lst)-1):
    print(lst[i], end=",")
print(lst[-1])