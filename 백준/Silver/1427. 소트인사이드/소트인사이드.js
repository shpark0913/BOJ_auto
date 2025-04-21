const T = require("fs").readFileSync(0, "utf-8").trim()

const arr = T.split("")

arr.sort((a, b) => b - a)

console.log(arr.join(""))