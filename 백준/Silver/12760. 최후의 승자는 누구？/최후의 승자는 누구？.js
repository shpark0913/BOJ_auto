const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let lines = [];
let lineCount = 0;
let n, m;

rl.on('line', (line) => {
  lines.push(line);
  lineCount++;
  
  if (lineCount === 1) {
    const [numN, numM] = line.split(' ').map(Number);
    n = numN;
    m = numM;
  }
  
  // Once we have read n+1 lines, we can process the data
  if (lineCount === n + 1) {
    rl.close();
  }
});

rl.on('close', () => {
  const [firstLine, ...rest] = lines;
  const [n, m] = firstLine.split(' ').map(Number);
  
  const player = [];
  const answer = Array(n).fill(0);
  const result = [];
  
  for (let i = 0; i < n; i++) {
    const tmp = rest[i].split(' ').map(Number).sort((a, b) => a - b);
    player.push(tmp);
  }
  
  for (let i = 0; i < m; i++) {
    const tmp = [];
    
    for (let j = 0; j < n; j++) {
      tmp.push(player[j][i]);
    }
    
    const mx = Math.max(...tmp);
    
    for (let j = 0; j < n; j++) {
      if (tmp[j] === mx) {
        answer[j] += 1;
      }
    }
  }
  
  const winner = Math.max(...answer);
  for (let i = 0; i < n; i++) {
    if (answer[i] === winner) {
      result.push(i + 1);
    }
  }
  
  console.log(result.join(' '));
});