import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chess_board = []

for _ in range(N):
    chess = input()
    chess_board.append(chess)

min_count = int(1e9)
WB = 'WBWBWBWB'
BW = 'BWBWBWBW'


def count_change_color(i, j):
    global min_count
    cnt_WB = 0
    cnt_BW = 0

    for a in range(8):
        if a % 2:
            for b in range(8):
                if chess_board[i + a][j + b] != WB[b]:
                    cnt_WB += 1
                if chess_board[i + a][j + b] != BW[b]:
                    cnt_BW += 1
        else:
            for b in range(8):
                if chess_board[i + a][j + b] != BW[b]:
                    cnt_WB += 1
                if chess_board[i + a][j + b] != WB[b]:
                    cnt_BW += 1

    if min(cnt_WB, cnt_BW) < min_count:
        min_count = min(cnt_WB, cnt_BW)


for i in range(N - 7):
    for j in range(M - 7):
        count_change_color(i, j)

print(min_count)
