# key: 기존 단어 , value: 치환될 단어 를 가지는 dictionary
wordDic = {}

for _ in range(N := int(input())):
    
    # '=' 를 기준으로 단어 분류, 좌측 단어를 key로 우측 단어를 value로 설정
    key, value = input().split("=")
    
    # '=' 를 기준으로 나눌 때 생기는 공백을 제거
    wordDic[key.strip()] = value.strip()

for _ in range(T := int(input())):
    N = int(input())
    
    # 정답이 될 string
    answerStr = ''
    sentence = list(input().split())
    for word in sentence:
        
        # answerStr에 치환되는 단어를 붙이고 뒤에 공백도 붙인다
        answerStr += (wordDic[word] + ' ')
        
    # 마지막 단어의 오른쪽 공백을 제거하고 출력한다.
    print(answerStr.rstrip())