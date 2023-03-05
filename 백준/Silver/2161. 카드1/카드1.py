# 카드 순서를 담는 리스트
cards = []
# 버려진 카드 순서를 담는 리스트
discard = []
for i in range(N := int(input())):
    cards.append(i+1)
    
if len(cards) == 1:
    print(1)
    exit(0)

while 1:
    # 카드를 하나 버린다
    throwCard = cards.pop(0)
    discard.append(throwCard)
    if len(cards) == 1: break
    # 남은 카드가 1개 초과라면 처음 카드를 맨 뒤로 보낸다
    card = cards.pop(0)
    cards.append(card)

print(*discard, end=' ')
print(cards[0])