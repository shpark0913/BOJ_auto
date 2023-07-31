case_num = 0
while 1:
    case_num += 1
    word1 = input()
    word2 = input()
    if word1 == word2 == "END":
        exit(0)
    word1_lst = sorted(list(word1))
    word2_lst = sorted(list(word2))
    if word1_lst == word2_lst:
        print(f'Case {case_num}: same')
    else:
        print(f'Case {case_num}: different')