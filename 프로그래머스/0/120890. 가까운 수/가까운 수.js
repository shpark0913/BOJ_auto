function solution(array, n) {
    let answer = 0;
    let distance = 1000;
    
    for (let i = 0; i < array.length; i++) {
        let currentDistance = Math.abs(n - array[i]);
        
        if (currentDistance < distance) {
            distance = currentDistance;
            answer = array[i];
        } 
        // 거리가 같으면 더 작은 값 선택
        else if (currentDistance === distance && array[i] < answer) {
            answer = array[i];
        }
    }
    
    return answer;
}