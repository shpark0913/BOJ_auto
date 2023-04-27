count = [0] * (1000 + 1)
s = 0 
for _ in range(10):
    num = int(input())
    s += num
    count[num] += 1

print(s // 10)  # 최대값
print(count.index(max(count)))