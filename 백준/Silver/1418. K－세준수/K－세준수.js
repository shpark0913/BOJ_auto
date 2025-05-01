const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let inputs = [];

rl.on('line', (line) => {
  inputs.push(line);
  if (inputs.length === 2) {
    const N = parseInt(inputs[0]);
    const K = parseInt(inputs[1]);
    
    const sosu = Array(100001).fill(true);
    
    for (let i = 2; i <= Math.sqrt(100000); i++) {
      if (sosu[i]) {
        let j = 2;
        while (i * j <= 100000) {
          sosu[i * j] = false;
          j++;
        }
      }
    }
    
    const k_num = Array(N + 1).fill(1);
    k_num[0] = 0;
    
    for (let i = 2; i <= N; i++) {
      if (sosu[i] && i > K) {
        for (let j = i; j <= N; j += i) {
          k_num[j] = 0;
        }
      }
    }
    
    console.log(k_num.reduce((a, b) => a + b, 0));
    
    rl.close();
  }
});