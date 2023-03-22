# 지구 : E (1 ~ 15), 태양 : S (1 ~ 28), 달 : M (1 ~ 19)
E, S, M = map(int, input().split())

year = max(E, S, M)

while 1:
    if year % 15:
        E_year = year % 15
    else:
        E_year = 15    
    if year % 28:
        S_year = year % 28
    else:
        S_year = 28   
    if year % 19:
        M_year = year % 19
    else:
        M_year = 19
    if [E_year, S_year, M_year] == [E, S, M]:
        print(year)
        break
    year += 1