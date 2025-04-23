const [T, ...members] = require("fs")
  .readFileSync(0, "utf-8")
  .trim()
  .split("\n")

const isAscending = (members) => {
  for (let i = 0; i < members.length - 1; i++) {
    if (members[i] > members[i + 1]) return false
  }
  return true
}

const isDescending = (members) => {
  for (let i = 0; i < members.length - 1; i++) {
    if (members[i] < members[i + 1]) return false
  }
  return true
}


const result = isAscending(members)
  ? "INCREASING"
  : isDescending(members)
  ? "DECREASING"
  : "NEITHER"

console.log(result)