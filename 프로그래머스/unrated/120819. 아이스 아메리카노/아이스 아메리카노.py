def solution(m):
    answer = [m // 5500, m - int(5500 * (m // 5500))]
    return answer