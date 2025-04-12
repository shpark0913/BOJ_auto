const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
const maxValue = Math.max(...input);
const maxIndex = input.findIndex((value) => value === maxValue);
console.log(maxValue);
console.log(maxIndex + 1);