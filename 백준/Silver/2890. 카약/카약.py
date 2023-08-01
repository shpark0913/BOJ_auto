R, C = map(int, input().split())

# lines = [list(input()) for _ in range(R)]

lines = []

for _ in range(R):
    line = list(input())
    if line != ['S'] + ["."] * (C - 2) + ["F"]:
        lines.append(line)

ranks = [0] * 10

rank = 1
exist = False
for i in range(C - 2, 0, -1):
    for line in lines:
        if line[i] != "." and ranks[int(line[i])] == 0:
            ranks[int(line[i])] = rank
            exist = True
    if exist:
        rank += 1
        exist = False

for rank in ranks[1:]:
    print(rank)