const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let line = 0;
const [N, M] = input[line++].split(' ').map(Number);

const arr = [];
for (let i = 0; i < N; i++) {
    arr.push(input[line++].split(' ').map(Number));
}

const K = Number(input[line++]);
for (let i = 0; i < K; i++) {
    let partialSum = 0;
    const [x1, y1, x2, y2] = input[line++].split(' ').map(Number);
    
    for (let r = x1 - 1; r <= x2 - 1; r++) {
        for (let c = y1 - 1; c <= y2 - 1; c++) {
            partialSum += arr[r][c];
        }
    }
    
    console.log(partialSum);
}