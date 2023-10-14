def solution(s):
    open, close = 0, 0
    for i in s:
        if i == "(":
            open += 1
        else:
            open -= 1
            if open < 0:
                return False
    if open == 0 and close == 0:
        return True
    
    return False