const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputLines = [];
let currentLine = 0;

rl.on('line', (line) => {
    inputLines.push(line.trim());
});

rl.on('close', () => {
    const [N, M, V] = inputLines[0].split(' ').map(Number);
    
    let dfsResult = [];
    let bfsResult = [];
    
    function dfs(graph, v, visited) {
        visited[v] = true;
        dfsResult.push(v);
        for (let i of graph[v]) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(graph, i, visited);
            }
        }
    }
    
    function bfs(graph, v, visited) {
        visited[v] = true;
        let queue = [v];
        
        while (queue.length > 0) {
            let q = queue.shift();
            bfsResult.push(q);
            for (let i of graph[q]) {
                if (!visited[i]) {
                    queue.push(i);
                    visited[i] = true;
                }
            }
        }
    }
    
    let graph = Array.from({ length: N + 1 }, () => []);
    
    for (let i = 1; i <= M; i++) {
        const [a, b] = inputLines[i].split(' ').map(Number);
        graph[a].push(b);
        graph[b].push(a);
    }
    
    for (let i = 0; i <= N; i++) {
        graph[i].sort((a, b) => a - b);
    }
    
    let visitedDfs = new Array(N + 1).fill(false);
    let visitedBfs = new Array(N + 1).fill(false);
    
    dfs(graph, V, visitedDfs);
    bfs(graph, V, visitedBfs);
    console.log(dfsResult.join(' '));
    console.log(bfsResult.join(' '));
});