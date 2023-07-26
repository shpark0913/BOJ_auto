for _ in range(TC := int(input())):
    J, N = map(int, input().split())
    boxes = []
    for _ in range(N):
        R, C = map(int, input().split())
        boxes.append(R * C)

    boxes.sort(reverse=True)

    cnt = 0
    candies = 0

    for box in boxes:
        candies += box
        cnt += 1
        if candies >= J:
            print(cnt)
            break