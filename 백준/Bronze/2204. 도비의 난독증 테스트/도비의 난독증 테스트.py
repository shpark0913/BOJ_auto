while 1:
    N = int(input())
    if not N: break
    words = {}
    words_lst = []
    for _ in range(N):
        s = input()
        words[s.lower()] = s
        words_lst.append(s.lower())
    for key in words.keys():
        if key == sorted(words_lst)[0]:
            print(words[key])
            break