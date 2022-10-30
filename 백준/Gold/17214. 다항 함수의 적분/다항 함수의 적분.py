s = input()
s_list = list(s[1:])
if 'x' not in s_list:
    if s == '0':
        print('W')
    elif s == '1':
        print('x+W')
    elif s == '-1':
        print('-x+W')
    else:
        print(s+'x+W')
else:
    if '+' in s_list or '-' in s_list:
        for i in range(1, len(s)):
            if s[i] in {'+', '-'}:
                front = s[:i]
                middle = s[i]
                back = s[i+1:]
                break
        if back != '0':
            if s[0] == '-':
                coef = int(front[1:-1])//2
                if coef == 1:
                    if back == '1':
                        print('-' + 'xx' + middle + 'x+W')
                    else:
                        print('-' + 'xx' + middle + back + 'x+W')
                else:
                    if back == '1':
                        print('-' + str(coef) + 'xx' + middle + 'x+W')
                    else:
                        print('-' + str(coef) + 'xx' + middle + back + 'x+W')
            else:
                coef = int(front[:-1])//2
                if coef == 1:
                    if back == '1':
                        print('xx' + middle + 'x+W')
                    else:
                        print('xx' + middle + back + 'x+W')
                else:
                    if back == '1':
                        print(str(coef) + 'xx' + middle + 'x+W')
                    else:
                        print(str(coef) + 'xx' + middle + back + 'x+W')
        else:
            s = front
            if s[0] == '-':
                coef = int(s[1:-1])//2
                if coef == 1:
                    print('-' + 'xx+W')
                else:
                    print('-' + str(coef) + 'xx+W')

            else:
                coef = int(s[:-1])//2
                if coef == 1:
                    print('xx+W')
                else:
                    print((str(coef)) + 'xx+W')

    else:
        if s[0] == '-':
            coef = int(s[1:-1])//2
            if coef == 1:
                print('-' + 'xx+W')
            else:
                print('-' + str(coef) + 'xx+W')

        else:
            coef = int(s[:-1])//2
            if coef == 1:
                print('xx+W')
            else:
                print((str(coef)) + 'xx+W')