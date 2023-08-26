s = input()

num_c = 26
num_d = 10
ans = 1

for i in range(len(s)):
    if s[i] == "c":
        ans_i = 26
    elif s[i] == "d":
        ans_i = 10
    if i:
        if s[i-1] == s[i]:
            ans_i -= 1
    ans *= ans_i

print(ans)