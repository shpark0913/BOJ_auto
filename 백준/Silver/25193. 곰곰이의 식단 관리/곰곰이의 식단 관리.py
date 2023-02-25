# 식단을 정할 일수
N = int(input())

# 음식의 리스트인 길이 N의 문자열
foods = input()

# C의 수
cnt_C = 0

for food in foods:
    if food == "C":
        cnt_C += 1

# C가 아닌 수
cnt = len(foods) - cnt_C

ans = (cnt_C)/(cnt+1)

if ans == int(ans):
    print(int(ans))
else:
    print((int(ans)+1))