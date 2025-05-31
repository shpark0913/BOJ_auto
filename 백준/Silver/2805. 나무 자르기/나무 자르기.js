const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let inputLines = [];
rl.on('line', (line) => {
  inputLines.push(line);
  if (inputLines.length === 2) {
    rl.close();
  }
});

rl.on('close', () => {
  const [N, M] = inputLines[0].split(' ').map(Number);
  const trees = inputLines[1].split(' ').map(Number).sort((a, b) => a - b);

  let start = 0;
  let end = trees[trees.length - 1];
  let result = 0;

  while (start <= end) {
    let total = 0;
    const mid = Math.floor((start + end) / 2);

    for (const tree of trees) {
      if (tree > mid) {
        total += tree - mid;
      }
    }

    if (total < M) {
      end = mid - 1;
    } else {
      result = mid;
      start = mid + 1;
    }
  }

  console.log(result);
});
