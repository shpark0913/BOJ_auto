for _ in range(N := int(input())):
    n = int(input())
    if str(n ** 2)[-len(str(n)):] == str(n):
        print("YES")
    else:
        print("NO")