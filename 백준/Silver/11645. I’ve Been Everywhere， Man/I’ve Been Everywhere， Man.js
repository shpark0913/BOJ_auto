const [T, ...inputs] = require("fs")
  .readFileSync(0, "utf-8").trim()
  .split("\n");

let visited = new Set()
for (let i = 0; i < inputs.length; i++) {
  // 숫자인 경우
  if (!isNaN(Number(inputs[i]))) {
    if (i === 0) continue
    console.log(visited.size)
    visited.clear()
  } else {
    visited.add(inputs[i])
  }

  if (i === inputs.length - 1) {
    console.log(visited.size)
  }
}
