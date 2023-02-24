# 알파벳 획 수
alphabet = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

# A, B 의 이름
nameA = input()
nameB = input()

# 이름 궁합 (A, B의 이름을 번갈아서)
loveName = ''

for i in range(len(nameA)):
    loveName += nameA[i]
    loveName += nameB[i]

# 이름 궁합 점수 계산하기
loveDigit = []
loveDigitCalculate = []

for i in range(len(loveName)):
    loveDigit.append(alphabet[loveName[i]])

while 1:
    for i in range(len(loveDigit)-1):
        sumDigit = loveDigit[i] + loveDigit[i+1]
        loveDigitCalculate.append(sumDigit % 10)
    loveDigit = loveDigitCalculate
    loveDigitCalculate = []
    if len(loveDigit) == 2:
        break

# 답을 ansStr에 문자열로 저장
ansStr = ''
for digit in loveDigit:
    ansStr += str(digit)
    
print(ansStr)