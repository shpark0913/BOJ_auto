const [T, ...inputs] = require("fs").readFileSync(0, "utf-8").trim().split("\n")

let index = 0

for (let i = 0; i < T; i++) {
  const N = Number(inputs[index++])
  const words = inputs.slice(index, index + N)
  index += N
  let result = "0"

  for (let i = 0; i < words.length; i++) {
    for (let j = 0; j < words.length; j++) {
      if (i === j) continue
      const combined = words[i] + words[j]
      if (combined === combined.split("").reverse().join("")) {
        result = combined
        break
      }
    }
    if (result !== "0") break
  }
  console.log(result)
}
