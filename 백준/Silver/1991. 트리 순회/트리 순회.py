N = int(input())
arr = [list(input().split()) for _ in range(N)]
c1 = [0] * (N+1)
c2 = [0] * (N+1)

def preorder(T):
    if T:
        print(chr(T+64), end='')
        preorder(c1[T])
        preorder(c2[T])

def inorder(T):
    if T:
        inorder(c1[T])
        print(chr(T+64), end='')
        inorder(c2[T])

def postorder(T):
    if T:
        postorder(c1[T])
        postorder(c2[T])
        print(chr(T+64), end='')

for elt in arr:
    if elt[1] != '.':
        c1[ord(elt[0]) - 64] = ord(elt[1])-64
    if elt[2] != '.':
        c2[ord(elt[0]) - 64] = ord(elt[2])-64

preorder(1)
print()
inorder(1)
print()
postorder(1)