const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();
console.log(processInput(input));

function calculateLaserIntensity(x1, x2, a, b, c, d, e) {
  function primitive(x) {
    return (
      (a * Math.pow(x, 3)) / 3 + ((b - d) * Math.pow(x, 2)) / 2 + (c - e) * x
    )
  }

  const result = primitive(x2) - primitive(x1)

  return Math.min(result, 1e9)
}

function processInput(input) {
  const lines = input.trim().split("\n")

  const [x1, x2] = lines[0].split(" ").map(Number)

  const [a, b, c, d, e] = lines[1].split(" ").map(Number)

  const intensity = calculateLaserIntensity(x1, x2, a, b, c, d, e)

  return intensity
}
