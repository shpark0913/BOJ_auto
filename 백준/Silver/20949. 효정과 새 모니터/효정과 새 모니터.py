import sys
input = sys.stdin.readline

# 모니터의 개수
N = int(input())

# 각 모니터의 가로 픽셀 수와 세로 픽셀 수를 원소로 가지는 리스트
monitors = []

for i in range(N):
    monitors.append([i+1, list(map(int, input().split()))])

for monitor in monitors:
    monitor.append((monitor[1][1]**2 + monitor[1][0]**2)**(1/2)/24)

monitors = sorted(monitors, key=lambda x:-x[-1])

for monitor in monitors:
    print(monitor[0])