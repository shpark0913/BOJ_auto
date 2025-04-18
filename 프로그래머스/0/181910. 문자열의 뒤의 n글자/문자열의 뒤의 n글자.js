function solution(my_string, n) {
    var answer = '';
    
    let reverse_my_string = my_string.split('').reverse().join('');
    
    for (let i = 0; i < n; i++) {
        answer += reverse_my_string[i];
    }
    
    return answer.split('').reverse().join("");
}