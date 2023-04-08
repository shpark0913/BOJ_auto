players = {}

for _ in range(N := int(input())):
    person = input()
    if person[0] not in players.keys():
        players[person[0]] = 1
    else:
        players[person[0]] += 1

canPlay = []

for player in players.keys():
    if players[player] >= 5:
        canPlay.append(player)

if not canPlay:
    print("PREDAJA")
    exit(0)

canPlay = sorted(canPlay)

for elt in canPlay:
    print(elt, end="")
