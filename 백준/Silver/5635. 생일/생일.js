let [n, ...studentsInput] = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

let students = [];
for (let student of studentsInput) {
    let [name, dd, mm, yy] = student.split(' ')
    students.push({name: name, year: +yy, month: +mm, day: +dd});
}
students.sort((a, b) => {
    return a.year - b.year || a.month - b.month || a.day - b.day;
})

console.log(`${students[students.length -1].name}\n${students[0].name}`);