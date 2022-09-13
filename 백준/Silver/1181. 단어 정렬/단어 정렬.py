N = int(input())

lst = {input() for _ in range(N)}
lst = list(lst)
lst.sort()
lst.sort(key=len)       # 길이로 정렬. sort() 1번 또 하면 알파벳 순
print("\n".join(lst))