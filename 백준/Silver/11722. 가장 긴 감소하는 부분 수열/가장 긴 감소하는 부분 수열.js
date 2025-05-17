const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
const totalCase = Number(lines[0]);
const inputs = lines[1].split(' ').map(v => Number(v));

const dp = [];

for (let i = 0; i< totalCase; i++) {
    let max = 0;
    
    for (let j = 0; j < i; j++) {
        if (inputs[i] < inputs[j] && dp[j] > max) {
            max = dp[j];
        }
    }
    
    dp[i] = max + 1;
}

console.log(Math.max(...dp));