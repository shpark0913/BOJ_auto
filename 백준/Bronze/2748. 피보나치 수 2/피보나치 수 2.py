N = int(input())

nums = [0] * 91

nums[1] = 1

for i in range(2, 91):
    nums[i] = nums[i-2] + nums[i-1]

print(nums[N])