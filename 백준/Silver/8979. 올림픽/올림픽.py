N, K = map(int, input().split())   # N : 국가의 수, K : 등수를 알고픈 국가

orders = []

for _ in range(N):
    orders.append(list(map(int, input().split())))

orders.sort(key=lambda x: (-x[1], -x[2], -x[3]))
orders = [[0]] + orders
grade = 0
grade_final = 0
for idx in range(len(orders)):
    if orders[idx][0] == K:
        grade = idx
        grade_final = idx

for idx in range(grade_final-1, 0, -1):
    if orders[grade_final][1:] == orders[idx][1:]:
        grade -= 1
    else:
        break
        
print(grade)