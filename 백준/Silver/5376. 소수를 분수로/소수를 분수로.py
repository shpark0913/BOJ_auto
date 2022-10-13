import fractions

T = int(input())

for t in range(T):
    s = input()
    if '(' in s:
        i = 0
        for j in range(len(s)):
            if s[j] == '(':
                i = j
                break
        s_part = s[i+1:len(s)-1]
        L = len(s)
        LP = len(s_part)
        if L-4 == LP:
            print(fractions.Fraction((int(s_part)), int('9'*(L-4))))
        else:
            print(fractions.Fraction((int(s[2:i]+s[i+1:L-1])-int(s[2:i])), int('9'*LP + '0'*(len(s)-4-LP))))
    else:
        L = len(s)
        print(fractions.Fraction(int(s[2:]), 10**(L-2)))
