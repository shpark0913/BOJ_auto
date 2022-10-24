A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)
dic = {
    '0' : 0,
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0,
}

for i in ABC:
    dic[i] += 1

for i in dic.values():
    print(i)