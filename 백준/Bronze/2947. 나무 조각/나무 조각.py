# 나무 조각 순서 담을 리스트
trees = list(map(int, input().split()))

while trees != [1, 2, 3, 4, 5]:
    for i in range(4):
        if trees[i] > trees[i + 1]:
            trees[i], trees[i + 1] = trees[i + 1], trees[i]
            print(*trees)
        if trees == [1, 2, 3, 4, 5]:
            exit(0)