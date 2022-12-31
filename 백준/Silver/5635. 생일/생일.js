let [n, ...studentsInput] = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

let students = [];
for (let student of studentsInput) {
    let [name, dd, mm, yy] = student.split(' ')
    students.push({name: name, year: +yy, month: +mm, day: +dd});
}
students.sort((a, b) => {
    if (a.year - b.year === 0) {
        if (a.month - b.month === 0) {
            return a.day - b.day;
        }
        return a.month - b.month;
    }
    return (a.year - b.year)
})

console.log(students[students.length -1].name);
console.log(students[0].name);