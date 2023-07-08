word = input()

cnt = 0

for i in range(len(word) - 1):
    if word[i:i+2] == "c=":
        cnt += 1
    elif word[i:i + 2] == "c-":
        cnt += 1
    elif i < len(word) - 2 and word[i:i+3] == "dz=":
        cnt += 1
    elif word[i:i+2] == "d-":
        cnt += 1
    elif word[i:i+2] == "lj":
        cnt += 1
    elif word[i:i+2] == "nj":
        cnt += 1
    elif word[i:i+2] == "s=":
        cnt += 1
    elif word[i:i+2] == "z=":
        cnt += 1

print(len(word) - cnt)