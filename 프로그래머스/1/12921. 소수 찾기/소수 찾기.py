def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if isPrime(i):
            answer += 1
    return answer