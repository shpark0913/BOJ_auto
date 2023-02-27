# 원래 알파벳
arr_before = list('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split())

# 카이사르 알파벳 (알파벳 문자 3개씩 건너뛰기)
arr_after = list('D E F G H I J K L M N O P Q R S T U V W X Y Z A B C'.split())

# 카이사르 암호 변환 후 알파벳
word_after = input()

# 본래 알파벳
word_before = ''

# 본래 알파벳으로 변환하기
for word in word_after:
    for i in range(len(arr_after)):
        if word == arr_after[i]:
            word_before += arr_before[i]
            break
print(word_before)
