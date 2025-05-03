const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const lst = [];
for (let i = 1; i <= N; i++) {
    lst.push(input[i]);
}

const arr = [];
for (let s of lst) {
    s = '0' + s;
    let word = '';
    for (let i = 1; i < s.length; i++) {
        if (s[i] !== s[i-1]) {
            word += s[i];
        }
    }
    arr.push(word);
}

let c = N;
for (let elt of arr) {
    const dic = {};
    for (let i of elt) {
        if (i in dic) {
            dic[i] += 1;
        } else {
            dic[i] = 1;
        }
    }
    
    for (let value of Object.values(dic)) {
        if (value > 1) {
            c -= 1;
            break;
        }
    }
}

console.log(c);