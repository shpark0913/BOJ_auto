N = int(input())
lstA = list(map(int, input().split()))
M = int(input())
lstB = list(map(int, input().split()))
dic = {}

for elt in lstA:
    if elt not in dic.keys():
        dic[elt] = 1

for elt in lstB:
    if elt in dic.keys():
        print(1)
    else: 
        print(0)