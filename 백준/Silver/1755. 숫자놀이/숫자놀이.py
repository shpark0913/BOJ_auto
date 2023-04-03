nums = [['0', 'zero'], ['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'], ['7', 'seven'], ['8', 'eight'], ['9', 'nine']]

M, N = map(int, input().split())

integers = []

for i in range(M, N+1):
    integers.append([str(i)])

integersStr = []

for i in range(len(integers)):
    integerStr = ''
    for j in integers[i]:
        for k in j:
            for num in nums:
                if num[0] == k:
                    integerStr += num[1]
    integers[i].append(integerStr)

integers.sort(key=lambda x:x[1])

for integer in integers:
    print(integer[0])