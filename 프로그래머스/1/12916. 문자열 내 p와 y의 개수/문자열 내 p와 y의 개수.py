def solution(s):
    answer = True
    
    num_p = s.count('p') + s.count('P')
    num_y = s.count('y') + s.count('Y')
    
    if num_p != num_y: answer = False

    return answer