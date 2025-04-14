const getSequenceValue = (a, d, n) => {
    return a + (n) * d
}

function solution(a, d, included) {
    let answer = 0;
    for (let i=0; i < included.length; i++) {
        if (included[i]) {
            answer = answer + getSequenceValue(a, d, i)
        }
    }
    return answer;
}