def isPrime(n):
    for i in range(2, int(n/2) + 1):
        # 소수 아닌 경우
        if not n % i:
            return False
    # 소수인 경우
    return True

N = int(input())

prime_list = list(map(int, input().split()))

prime_cnt = 0

for num in prime_list:
    if isPrime(num) and num > 1:
        prime_cnt += 1

print(prime_cnt)