import sys
inputFast = sys.stdin.readline

# 저장된 사이트 주소의 수, 비밀번호 찾으려는 사이트 주소의 수
N, M = map(int, inputFast().split())

informations = {}

for _ in range(N):
    address, pw = inputFast().split()
    informations[address] = pw

for _ in range(M):
    isAddress = input().rstrip()
    print(informations[isAddress])
