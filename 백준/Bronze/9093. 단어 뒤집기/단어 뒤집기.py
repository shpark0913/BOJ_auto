N = int(input())

for _ in range(N):
    lst = list(input().split())
    lst_inverse = []
    for elt in lst:
        lst_inverse.append(elt[::-1])
    for i in range(len(lst_inverse)-1):
        print(lst_inverse[i], end=' ')
    print(lst_inverse[-1])