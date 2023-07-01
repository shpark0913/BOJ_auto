import math
import sys
input = sys.stdin.readline

N = int(input())

# 15의 배수라면, 3의 배수와 5의 배수여야 함
# 3의 배수는 모든 자릿수의 합이 3의 배수
# 5의 배수는 일의 자리가 0 또는 5

nums = [5] * N

can_answer = set()

num_1 = 0

while 1:
    if sum(nums) % 3 == 0:
        can_answer.add(N - num_1)
    num_1 += 1
    nums = [1] * num_1 + [5] * (N - num_1)
    if nums == [1] * N:
        break

if not can_answer:
    print(0)
else:
    ans = 0
    for elt in can_answer:
        if elt:
            ans += math.comb(N - 1, elt - 1)
    print(ans % 1000000007)
