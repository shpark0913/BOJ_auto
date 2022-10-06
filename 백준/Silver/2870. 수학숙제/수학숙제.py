N = int(input())
lst = [list(input()) for _ in range(N)]
arr = []

for elt in lst:
    s = ''
    for i in range(len(elt)):
        if elt[i].isalpha():
            s += '_'
        else:
            s += elt[i]
    arr.append(s)

arr2 = []
for elt in arr:
    elt2 = list(elt.split('_'))
    arr2.append(elt2)
arr3 = []

for elt in arr2:
    for element in elt:
        if element != '':
            element = int(element)
            arr3.append(element)

arr3.sort()
for elt in arr3:
    print(elt)