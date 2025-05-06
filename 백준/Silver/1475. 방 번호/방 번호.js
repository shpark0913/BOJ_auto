const fs = require('fs');
const roomNum = fs.readFileSync('/dev/stdin').toString().trim();

const nums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0};

for (let i = 0; i < roomNum.length; i++) {
    nums[parseInt(roomNum[i])]++;
}

if ((nums[6] + nums[9]) % 2) {
    nums[6] = Math.floor((nums[6] + nums[9]) / 2) + 1;
    nums[9] = 0;
} else {
    nums[6] = (nums[6] + nums[9]) / 2;
    nums[9] = 0;
}

console.log(Math.max(...Object.values(nums)));