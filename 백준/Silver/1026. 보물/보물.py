# 길이가 N인 정수 배열 A, B를 각각 리스트로 만들자
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

# 정답은 ans로 표현
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)