const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
let N, start, end, M;
let graph = [];
let visited = [];

rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    N = parseInt(lines[0]);
    [start, end] = lines[1].split(' ').map(Number);
    M = parseInt(lines[2]);
    
    graph = Array.from({ length: N + 1 }, () => []);
    visited = Array(N + 1).fill(0);
    
    for (let i = 3; i < 3 + M; i++) {
        const [a, b] = lines[i].split(' ').map(Number);
        graph[a].push(b);
        graph[b].push(a);
    }
    
    dfs(graph, visited, start);
    
    console.log(visited[end] ? visited[end] : -1);
});

function dfs(graph, visited, v) {
    for (const j of graph[v]) {
        if (!visited[j]) {
            visited[j] = visited[v] + 1;
            dfs(graph, visited, j);
        }
    }
}