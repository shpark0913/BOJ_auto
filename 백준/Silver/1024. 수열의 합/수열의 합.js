const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

rl.on("line", (line) => {
  const [N, L] = line.split(" ").map(Number)

  let _L = L

  while (true) {
    const a = (1 - _L) / 2 + N / _L

    if (a < 0 || _L > 100) {
      console.log(-1)
      break
    }

    if (a === Math.floor(a)) {
      const sequence = []
      for (let i = 0; i < _L; i++) {
        sequence.push(Math.floor(a + i))
      }
      console.log(sequence.join(" "))
      break
    } else {
      _L += 1
    }
  }

  rl.close()
})
