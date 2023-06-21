# 저장된 사이트 주소의 수, 비밀번호 찾으려는 사이트 주소의 수
N, M = map(int, input().split())

informations = {}

for _ in range(N):
    address, pw = input().split()
    informations[address] = pw

for _ in range(M):
    isAddress = input()
    print(informations[isAddress])