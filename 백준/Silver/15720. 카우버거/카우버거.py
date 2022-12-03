B, C, D = map(int, input().split())

prices_burger = sorted(list(map(int, input().split())), reverse=True)

prices_side = sorted(list(map(int, input().split())), reverse=True)

prices_drink = sorted(list(map(int, input().split())), reverse=True)
print(sum(prices_drink + prices_side + prices_burger))
min_num = min(B, C, D)

for i in range(min_num):
    prices_burger[i] *= 0.9
    prices_side[i] *= 0.9
    prices_drink[i] *= 0.9

prices_all = int(sum(prices_drink) + sum(prices_side) + sum(prices_burger))

print(prices_all)