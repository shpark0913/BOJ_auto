import sys
input = sys.stdin.readline

while 1:
    try:
        roomNumMin, roomNumMax = map(int, input().split())
        cnt = 0 # 반복되는 숫자가 없는 roomNum의 개수
        for roomNum in range(roomNumMin, roomNumMax + 1):
            isRoom = 1
            if roomNum >= 10:
                for i in range(len(str(roomNum)) - 1):
                    for j in range(i+1, len(str(roomNum))):
                        if str(roomNum)[i] == str(roomNum)[j]:
                            isRoom -= 1
            if isRoom == 1:
                cnt += 1
        print(cnt)
    except:
        exit(0)