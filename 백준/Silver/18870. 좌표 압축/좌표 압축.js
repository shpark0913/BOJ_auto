const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]); 
const lst = input[1].split(' ').map(Number);

let lst2 = Array.from(new Set(lst));
lst2.sort((a, b) => a - b); //

const dic = {};
for (let i = 0; i < lst2.length; i++) {
    dic[lst2[i]] = i;
}

let result = lst.map(elt => dic[elt]).join(' ');
console.log(result);
