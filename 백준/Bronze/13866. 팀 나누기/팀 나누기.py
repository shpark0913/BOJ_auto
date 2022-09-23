lst = list(map(int,input().split()))
lst.sort()

print(abs((lst[-1] + lst[0]) - (lst[2] + lst[1])))