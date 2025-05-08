const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const canvas = Array(100).fill().map(() => Array(100).fill(0));
let cnt = 0;
let inputCount = 0;

rl.on('line', (line) => {
    const [x1, y1, x2, y2] = line.split(' ').map(Number);
    
    for (let i = x1; i < x2; i++) {
        for (let j = y1; j < y2; j++) {
            if (canvas[i][j] === 1) {
                continue;
            }
            canvas[i][j] = 1;
            cnt += 1;
        }
    }
    
    inputCount++;
    
    if (inputCount === 4) {
        console.log(cnt);
        rl.close();
    }
});