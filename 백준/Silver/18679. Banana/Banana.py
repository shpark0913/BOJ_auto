wordDic = {}

for _ in range(N := int(input())):
    key, value = input().split("=")
    wordDic[key.strip()] = value.strip()

for _ in range(T := int(input())):
    N = int(input())
    answerStr = ''
    sentence = list(input().split())
    for word in sentence:
        answerStr += (wordDic[word] + ' ')
    print(answerStr.rstrip())