words = [input() for _ in range(5)]

max_length = 0

ans_list = []

for word in words:
    if max_length < len(word):
        max_length = len(word)

for i in range(max_length):
    for word in words:
        try:
            ans_list.append(word[i])
        except:
            pass

for ans in ans_list:
    print(ans, end="")