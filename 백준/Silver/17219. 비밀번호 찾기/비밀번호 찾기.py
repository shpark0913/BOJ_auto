import sys
input = sys.stdin.readline

N, M = map(int, input().split())

information_dic = {}

for _ in range(N):
    url, pw = input().split()
    information_dic[url] = pw

for _ in range(M):
    print(information_dic[input().rstrip()])
