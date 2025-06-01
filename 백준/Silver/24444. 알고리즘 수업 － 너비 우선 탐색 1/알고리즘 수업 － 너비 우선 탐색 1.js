const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', (line) => {
    input.push(line);
});

rl.on('close', () => {
    const [N, M, R] = input[0].split(' ').map(Number);
    
    let visited = new Array(N + 1).fill(0);
    let graph = Array.from({length: N + 1}, () => []);
    let cnt = 0;
    let dic = {};
    
    function BFS(v) {
        let queue = [];
        queue.push(v);
        
        while (queue.length > 0) {
            v = queue.shift();
            visited[v] = 1;
            cnt += 1;
            dic[v] = cnt;
            
            for (let i of graph[v]) {
                if (!visited[i]) {
                    visited[i] = 1;
                    queue.push(i);
                }
            }
        }
    }
    
    for (let i = 1; i <= M; i++) {
        const [u, v] = input[i].split(' ').map(Number);
        graph[u].push(v);
        graph[v].push(u);
    }
    
    for (let i = 1; i <= N; i++) {
        graph[i].sort((a, b) => a - b);
    }
    
    BFS(R);
    
    for (let i = 1; i <= N; i++) {
        if (i in dic) {
            console.log(dic[i]);
        } else {
            console.log(0);
        }
    }
});