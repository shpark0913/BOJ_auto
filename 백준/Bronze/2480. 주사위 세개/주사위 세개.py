dice_lst = list(map(int, input().split()))
dice = set(dice_lst)

if len(dice) == 1:
    print(10000 + dice_lst[0] * 1000)
elif len(dice) == 2:
    if dice_lst[0] == dice_lst[1]:
        print(1000 + dice_lst[0]*100)
    elif dice_lst[0] == dice_lst[2]:
        print(1000 + dice_lst[0]*100)
    elif dice_lst[1] == dice_lst[2]:
        print(1000 + dice_lst[1]*100)
else:
    print(max(dice)*100)