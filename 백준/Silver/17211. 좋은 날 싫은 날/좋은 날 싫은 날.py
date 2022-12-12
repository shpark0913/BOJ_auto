N, now = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

if not now: good = gg
else: good = bg

if N > 1:
    for _ in range(N-1):
        good = good*gg + (1-good)*bg

bad = 1000*(1-good)
good *= 1000
print(int(good))
print(int(bad))