l = int(input())
r = int(input())
k = int(input())
c = 0
if k == 2:
    if l <= 2:
        c = r - 3 + 1
        print(c) if c > 0 else print(0)
    else:
        c = r - l + 1
        print(c) if c > 0 else print(0)

elif k == 3:
    if l <= 5:
        c = r//3 - 2 + 1
        print(c) if c > 0 else print(0)
    else:
        if l % 3:
            c = r//3 - l//3
            print(c) if c > 0 else print(0)
        else:
            c = r//3 - l//3 + 1
            print(c) if c > 0 else print(0)

elif k == 4:
    if l <= 9:
        if l <= 12 <= r:
            c = r//2 - 5
            print(c) if c > 0 else print(0)
        else:
            c = r//2 - 5 + 1
            print(c) if c > 0 else print(0)
    else:
        if l % 2:
            if l <= 12 <= r:
                c = r//2 - l//2 - 1
                print(c) if c > 0 else print(0)
            else:
                c = r//2 - l//2
                print(c) if c > 0 else print(0)
        else:
            if l <= 12 <= r:
                c = r//2 - l//2
                print(c) if c > 0 else print(0)
            else:
                c = r//2 - l//2 + 1
                print(c) if c > 0 else print(0)

elif k == 5:
    if l < 15:
        c = r//5 - 3 + 1
        print(c) if c > 0 else print(0)
    else:
        if l % 5:
            c = r//5 - l//5
            print(c) if c > 0 else print(0)
        else:
            c = r//5 - l//5 + 1
            print(c) if c > 0 else print(0)