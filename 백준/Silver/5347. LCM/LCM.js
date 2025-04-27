const [T, ...inputs] = require("fs")
  .readFileSync(0, "utf-8")
  .trim()
  .split("\n");

for (const input of inputs) {
  const [a, b] = input.split(" ").map(Number);

  const gcd = (x, y) => {
    while (y) {
      [x, y] = [y, x % y];
    }
    return x;
  };

  const lcm = (x, y) => (x * y) / gcd(x, y);

  const result = lcm(a, b);
  console.log(result);
}
