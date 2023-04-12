real_div = int(input())              # 진짜 약수들의 개수
lst = list(map(int,input().split())) # 진짜 약수들
# lst.sort()
# print(lst[0]*lst[-1])
print(min(lst)*max(lst))