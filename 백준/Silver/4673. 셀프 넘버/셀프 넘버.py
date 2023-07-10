import sys
input = sys.stdin.readline

nums = list(range(1, 10001))

not_self = set()

for num in nums:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        not_self.add(num)

for num in not_self:
    nums.remove(num)

for num in nums:
    print(num)