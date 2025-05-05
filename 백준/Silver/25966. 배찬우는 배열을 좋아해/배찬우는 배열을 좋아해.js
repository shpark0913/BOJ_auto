const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let line = 0;
const [N, M, q] = input[line++].split(' ').map(Number);

const arr = [];
for (let i = 0; i < N; i++) {
    arr.push(input[line++].split(' ').map(Number));
}

for (let i = 0; i < q; i++) {
    const query = input[line++].split(' ').map(Number);
    
    if (query[0] === 1) {
        [arr[query[1]], arr[query[2]]] = [arr[query[2]], arr[query[1]]];
    } else {
        arr[query[1]][query[2]] = query[3];
    }
}

for (const row of arr) {
    console.log(row.join(' '));
}