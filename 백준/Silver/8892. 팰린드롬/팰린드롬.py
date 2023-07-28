def isPal(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            isAns = arr[i] + arr[j]
            if i != j and isAns == isAns[::-1]:
                return isAns
    return 0

for _ in range(N := int(input())):
    words = []
    for _ in range(T := int(input())):
        words.append(input())

    print(isPal(words))
