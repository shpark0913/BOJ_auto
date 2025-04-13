let fs = require('fs');
let input = Number(fs.readFileSync('/dev/stdin').toString().trim());
let factorial = 1;

for (let i = 1; i <= input; i++) {
    factorial *= i;
}

const secondsInWeek = 7 * 24 * 60 * 60;

let weeks = factorial / secondsInWeek;

console.log(Math.floor(weeks));