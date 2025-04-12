const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i = 0; i < input.length; i++) {
    // 공백으로 분리하고 숫자로 변환
    const line = input[i].trim().split(" ").map(Number);
    
    const countZero = line.filter(val => val === 0).length;
    
    let result;
    switch (countZero) {
        case 1: result = "A"; break;
        case 2: result = "B"; break;
        case 3: result = "C"; break;
        case 4: result = "D"; break;
        case 0: result = "E"; break;
        default: result = "E";
    }
    
    console.log(result);
}