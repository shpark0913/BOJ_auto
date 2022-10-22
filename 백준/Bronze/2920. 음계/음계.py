L = list(map(int, input().split()))
L2 = [1, 2, 3, 4, 5, 6, 7, 8]

if L == L2:
    print('ascending')
elif L == L2[::-1]:
    print('descending')
else:
    print('mixed')