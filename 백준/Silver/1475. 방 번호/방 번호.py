# 다솜이의 방 번호
roomNum = str(input())

# 다솜이 방 번호를 구성하는 숫자들의 개수
nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}

for num in roomNum:
    nums[int(num)] += 1

# 6, 9의 총 개수가 홀수라면
if (nums[6] + nums[9]) % 2:
    nums[6] = (nums[6] + nums[9])//2 + 1
    nums[9] = 0
else:
    nums[6] = (nums[6] + nums[9])//2
    nums[9] = 0

print(max(nums.values()))