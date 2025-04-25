const [...inputs] = require("fs").readFileSync(0, "utf-8").trim().split("\n")

for (const input of inputs) {
  const [s, t] = input.split(" ")

  let i = 0
  let j = 0
  while (i < s.length && j < t.length) {
    if (s[i] === t[j]) {
      i++
      j++
    } else {
      j++
    }
  }
  if (i === s.length) {
    console.log("Yes")
  } else {
    console.log("No")
  }
}
