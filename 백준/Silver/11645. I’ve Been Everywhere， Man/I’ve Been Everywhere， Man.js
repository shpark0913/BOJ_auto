const [T, ...inputs] = require("fs")
  .readFileSync(0, "utf-8").trim()
  .split("\n");

for (let i = 0; i < inputs.length; i++) {
  if (!isNaN(Number(inputs[i]))) {
    let visited = new Set()
    for (let j = i + 1; j < Number(inputs[i]) + i + 1; j++) {
      visited.add(inputs[j])
    }
    console.log(visited.size)
  }
}