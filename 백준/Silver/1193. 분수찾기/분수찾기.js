const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('', (input) => {
  const X = parseInt(input);
  let n = 1;
  
  while (true) {
    if ((n**2 - n + 2)/2 <= X && X < ((n+1)**2 - (n+1) + 2)/2) {
      break;
    }
    n += 1;
  }
  
  const d = X - Math.floor((n**2 - n + 2)/2);
  const w = String(1 + d);
  const p = String(n - d);
  
  if (n % 2) {
    console.log(p + "/" + w);
  } else {
    console.log(w + "/" + p);
  }
  
  readline.close();
});