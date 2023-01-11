N, M = map(int, input().split())

if N < M:
    print('TLE!')

else:
    if M <= 2: print("NEWBIE!")
    else: print("OLDBIE!")