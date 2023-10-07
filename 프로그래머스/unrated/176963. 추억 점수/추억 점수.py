def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        scores = 0
        for person in people:
            for i in range(len(name)):
                if name[i] == person:
                    scores += yearning[i]
        answer.append(scores)
    
    return answer