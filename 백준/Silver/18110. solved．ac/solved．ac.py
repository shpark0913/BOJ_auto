N = int(input())
opinions = sorted([int(input()) for _ in range(N)])

if not opinions:
    print(0)
else:
    delete = len(opinions) * 0.15
    if delete - int(delete) < 0.1:
        opinions = opinions[int(delete):len(opinions)-int(delete)]
    else:
        a = delete - int(delete)
        b = int(delete) + 1 - delete

        if a < b:
            delete = int(delete)
            opinions = opinions[int(delete):len(opinions) - int(delete)]

        else:
            delete = int(delete) + 1
            opinions = opinions[int(delete):len(opinions) - int(delete)]

    ans = sum(opinions)/len(opinions)
    alpha = ans - int(ans)
    beta = int(ans) + 1 - ans
    if alpha < beta:
        print(int(ans))
    else:
        print(int(ans) + 1)
