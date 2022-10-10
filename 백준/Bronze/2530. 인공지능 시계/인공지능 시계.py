H, M, S = map(int, input().split())
N = int(input())

time = 3600 * H + 60 * M + S + N

H1 = (time//3600)
M1 = (time-H1*3600)//60
S1 = (time-H1*3600-M1*60)
print(H1%24, M1, S1)