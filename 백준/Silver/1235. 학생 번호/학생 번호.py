stuNums = []

for _ in range(N := int(input())):
    stuNums.append(input())

l = len(stuNums[0])

for i in range(1, l+1):
    stuNumsSet = set()
    for num in stuNums:
        stuNumsSet.add(num[l-i:])
    if len(stuNumsSet) == N:
        print(i)
        exit(0)