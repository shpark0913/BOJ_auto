import sys
input = sys.stdin.readline

# 방의 크기
N, M = map(int, input().split())

# 처음 로봇 좌표 및 로봇 청소기가 바라보는 방향
# d가 [0, 1, 2, 3] -> [북, 동, 남, 서]
r, c, d = map(int, input().split())

# 방의 상태 (0 : 청소 전, 1 : 벽, 2 : 청소 후)
area = []

clean_num = 0

for _ in range(N):
    area.append(list(map(int, input().split())))


def clean(x, y, s):
    global clean_num
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction = [0, 1, 2, 3]  # 북, 동, 남, 서

    # 아직 청소 전 상태이면, 현재 칸을 청소
    if area[x][y] == 0:
        area[x][y] = 2
        clean_num += 1

    # 동서남북 4곳의 상태를 담는 리스트
    near_4 = []

    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
            near_4.append(area[x + dx[i]][y + dy[i]])
    # 주변 칸 중 청소되지 않은 빈 칸이 없는 경우 (다 청소된 경우)
    if 0 not in near_4:
        for i in range(4):
            if direction[i] == s:
                if 0 <= x - dx[i] < N and 0 <= y - dy[i] < M and area[x - dx[i]][y - dy[i]] != 1:
                    clean(x - dx[i], y - dy[i], s)
                else:
                    return

    # 주변 칸 중 청소되지 않은 빈 칸이 있는 경우 (더 청소해야 함)
    else:
        for _ in range(4):
            s -= 1
            if s < 0:
                s = 3
            nx = x + dx[s]
            ny = y + dy[s]
            if 0 <= nx < N and 0 <= ny < M:
                if area[nx][ny] == 0:
                    clean(nx, ny, s)
                    break


clean(r, c, d)

print(clean_num)
