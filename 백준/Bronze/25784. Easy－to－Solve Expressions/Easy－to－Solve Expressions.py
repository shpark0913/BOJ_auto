arr = list(map(int,input().split()))
def f():
    mul = (arr[0] * arr[1] * arr[2])
    for i in range(3):
        if 2*arr[i] == sum(arr):
            print(1)
            return
        if arr[i] * arr[i] == mul:
            print(2)
            return
    print(3)
    return
f()