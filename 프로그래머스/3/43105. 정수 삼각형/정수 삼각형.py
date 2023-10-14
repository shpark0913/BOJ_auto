def solution(triangle):
    if len(triangle) == 1:
        return max(triangle[0])
    
    for k in range(1, len(triangle)):
        triangle[k][0] += triangle[k - 1][0]
    
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i])):
            if j != (len(triangle[i]) - 1):
                triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j], triangle[i][j] + triangle[i - 1][j - 1])     
            else:
                triangle[i][j] += triangle[i - 1][j - 1]

    return max(triangle[-1])