const [T, ...inputs] = require("fs").readFileSync(0, "utf-8").trim().split("\n")

const result = inputs.filter((input) => {
  return (input + input).includes(T)
}).length

console.log(result)
