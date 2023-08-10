N = int(input())

arr = [i for i in range(1, N + 1)]

new_arr = []

while 1:
    if len(arr) == 1:
        print(arr[0])
        break

    for i in range(len(arr)):
        if i % 2:
            new_arr.append(arr[i])
    arr = new_arr
    new_arr = []