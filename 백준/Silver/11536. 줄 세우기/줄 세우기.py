names = []
for _ in range(N := int(input())):
    names.append(input())

names_sort = sorted(names)
names_sort_reverse = sorted(names, reverse=True)

if names == names_sort:
    print("INCREASING")
elif names == names_sort_reverse:
    print("DECREASING")
else:
    print("NEITHER")