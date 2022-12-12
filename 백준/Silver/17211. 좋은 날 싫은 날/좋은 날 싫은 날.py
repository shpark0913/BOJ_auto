N, now = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

if not now:
    good = gg
    bad = gb
else:
    good = bg
    bad = bb

if N > 1:
    for _ in range(N-1):
        good_new = good*gg + bad*bg
        bad_new = good*gb + bad*bb
        good = good_new
        bad = bad_new

good *= 1000
bad *= 1000
if 10*good - 10*int(good) >= 5:
    good = int(good) + 1
else:
    good = int(good)

if 10*bad - 10*int(bad) >= 5:
    bad = int(bad) + 1
else:
    bad = int(bad)
print(good, bad)