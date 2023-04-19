s = input()

numSmile = 0
numSad = 0

for i in range(len(s)-2):
    if s[i] == ":":
        if s[i+1:i+3] == "-)":
            numSmile += 1
        elif s[i+1:i+3] == "-(":
            numSad += 1

if numSad < numSmile:
    print("happy")
elif numSad == 0 and numSmile == 0:
    print("none")
elif numSad == numSmile:
    print("unsure")
else:
    print("sad")