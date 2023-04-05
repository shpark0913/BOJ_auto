cnt = 0

move = []

for _ in range(N := int(input())):
    cowNum, cowPlace = map(int, input().split())
    if len(move):
        for elt in move[::-1]:
            if elt[0] == cowNum:
                if elt[1] != cowPlace:
                    cnt += 1
                break
    move.append([cowNum, cowPlace])

print(cnt)