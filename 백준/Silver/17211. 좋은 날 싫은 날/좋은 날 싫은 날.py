N, now = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

if not now: good = gg
else: good = bg

if N > 1:
    for _ in range(N-1):
        good = good*gg + (1-good)*bg

bad = 1000*(1-good)
good *= 1000

if 10*good - 10*int(good) >= 5:
    good = int(good) + 1
else:
    good = int(good)
if 10*bad - 10*int(bad) >= 5:
    bad = int(bad) + 1
else:
    bad = int(bad)
print(good)
print(bad)