num_A, num_B = map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
a = len(set_A)
b = len(set_B)
for elt in set_B:
    set_A.add(elt)
c = len(set_A)

print((c-a) + (c-b))