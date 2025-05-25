const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    const [A, B] = line.split(' ').map(Number);
    let ans = -1;
    const queue = [[A, 1]];
    
    while (queue.length > 0) {
        const [a, b] = queue.shift();
        
        if (a === B) {
            ans = b;
            break;
        }
        
        if (a * 2 <= B) {
            queue.push([a * 2, b + 1]);
        }
        
        if (parseInt(a.toString() + '1') <= B) {
            queue.push([parseInt(a.toString() + '1'), b + 1]);
        }
    }
    
    console.log(ans);
    rl.close();
});