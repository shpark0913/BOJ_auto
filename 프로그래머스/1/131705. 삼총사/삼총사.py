from itertools import combinations

def solution(number):
    answer = 0
    for elt in list(combinations(number, 3)):
        if sum(elt) == 0:
            answer += 1
    return answer