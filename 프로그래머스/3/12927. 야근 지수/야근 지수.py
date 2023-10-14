import heapq

def solution(n, works):
    q = []
    for work in works:
        heapq.heappush(q, (-work, 0))
    for _ in range(n):
        if q:
            i = heapq.heappop(q)
            if i[0] != 0:
                heapq.heappush(q, (i[0] + 1, 0))
    answer = 0
    for elt in q:
        if elt[0] <= 0:
            answer += (elt[0] ** 2)
    
    return answer