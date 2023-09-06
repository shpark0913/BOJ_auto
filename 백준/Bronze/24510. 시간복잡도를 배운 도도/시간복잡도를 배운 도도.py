C = int(input())
max_value = 0
for _ in range(C):
    s = input()
    cnt_for = s.count('for')
    cnt_while = s.count('while')
    if max_value < cnt_for + cnt_while:
        max_value = cnt_for + cnt_while

print(max_value)