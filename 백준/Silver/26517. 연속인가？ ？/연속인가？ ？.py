k = int(input())
a, b, c, d = list(map(int, input().split()))

left = a * k + b
right = c * k + d

if left == right:
    print("Yes",right)
else:
    print("No")