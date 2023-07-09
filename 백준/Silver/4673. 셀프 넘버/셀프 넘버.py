nums = list(range(1, 10001))

not_self = []

for num in nums:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        not_self.append(num)

for num in set(not_self):
    nums.remove(num)

for num in nums:
    print(num)